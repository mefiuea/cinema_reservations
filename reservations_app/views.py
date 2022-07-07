from datetime import date
from random import randrange

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist

from .models import RepertoireModel, ReservationModel, SeatModel
from custom.get_booked_seats import get_booked_seats


def home_view(request):
    """Function to redirect user to repertoire view when he enters only the domain name."""

    return redirect(reverse_lazy('reservations_app:repertoire_view'))


def repertoire_view(request):
    """Function that displays repertoire when a date is selected.
    It also allows to use simple sorting and filtering."""

    if request.method == 'POST':
        pass

    if request.method == 'GET':
        # default variable declarations
        genres_list = []
        calendar_error = ''

        # get date selected by user
        date_selected = request.GET.get('date')
        # validate date
        if date_selected is None or date_selected == '':
            # when there is a problem with the date (will not pass validation) then assign today's date
            date_selected = date.today().strftime('%Y-%m-%d')

        # get repertoires (movies) from db for a given day with default sorting by screening day
        repertoires = RepertoireModel.objects.filter(screening_date=date_selected).order_by('screening_time')

        # get genres of movies for specific repertoire - used to list available filters
        for repertoire in repertoires:
            for genre in repertoire.movie.genre.all():
                # add genre to list
                genres_list.append((genre.genre, genre.id))
        # remove duplications of genres from list
        genres_list = list(dict.fromkeys(genres_list))

        context = {
            'date_selected': date_selected,
            'calendar_error': calendar_error,
            'repertoires': repertoires,
            'genres': genres_list,
        }
        return render(request, 'reservations_app/repertoire.html', context=context)


def get_repertoire_by_selected_sorting(request):
    """Function called (in background) by javascript 'sorting_repertoire.js' when clicking on sorting or filtering
    on the repertoire page. Its task is to sort and filter the current repertoire according to user settings."""

    # collecting information sent by javascript
    selected_sorting = request.GET.get('sorting_by')
    selected_date = request.GET.get('date')
    selected_genre = request.GET.get('genre')

    # validation for date
    if selected_date is None or selected_date == '':
        # when there is a problem with the date (will not pass validation) then assign today's date
        selected_date = date.today().strftime('%Y-%m-%d')

    # validation for sorting and assigning correct instructions for database
    if selected_sorting == 'screening_time':
        order_by = 'screening_time'
    elif selected_sorting == 'alphabetically':
        order_by = 'movie__title'
    elif selected_sorting == 'duration':
        order_by = 'movie__duration'
    else:
        order_by = 'screening_time'

    # validation for genre
    if selected_genre is None or selected_genre == 'None':
        selected_genre = 'no_filter'

    # start filtering and sorting (database query) depending on the selected settings
    if selected_genre == 'no_filter':
        # query without filter, but with selected sorting
        repertoires = RepertoireModel.objects.filter(screening_date=selected_date).order_by(order_by)
    else:
        # use genre filter and selected sorting
        repertoires = RepertoireModel.objects.filter(screening_date=selected_date,
                                                     movie__genre=selected_genre).order_by(order_by)

    context = {
        'repertoires': repertoires,
    }

    # render results into a template, from which the java script takes all the html code and inserts it into repertoire
    return render(request, 'reservations_app/repertoires_list_by_query_string.html', context=context)


def booking_view(request, repertoire_id):
    """Function that renders a view of the specific cienema hall. Called when the 'Go to cinema hall' button is pressed
    on the repertoire page."""

    if request.method == 'POST':
        pass

    if request.method == 'GET':
        # get repertoire id of chosen movie passed in the url
        repertoire_id = repertoire_id
        # get specific repertoire (movie) from database
        repertoire = RepertoireModel.objects.get(pk=repertoire_id)

        # get all reservations for this specific screening used to transfer list of reserved seats to html
        reservations = ReservationModel.objects.filter(repertoire=repertoire)
        # get all booked seats to list from custom function
        # return list
        booked_seats_list = get_booked_seats(reservation_instance=reservations)

        # get information about all dates to prevent reservations for an outdated date
        # get actual date
        actual_date = date.today()
        # get screening date
        screening_date = repertoire.screening_date
        # calculation of the difference of days until screening
        dif_date = (screening_date - actual_date).days

        context = {
            'repertoire_id': repertoire_id,
            'repertoire': repertoire,
            'booked_seats': booked_seats_list,
            'dif_date': dif_date,
        }
        return render(request, 'reservations_app/booking.html', context=context)


def booking_completed_view(request, repertoire_id):
    """Function used to save reservations for a given user with selected seats to database.
    Called by pressing 'Book ticket!' button in cinema hall view."""

    if request.method == 'POST':
        # get information about user
        buyer = request.user
        # get information about selected seats from checkbox list. Checkboxes are hidden in cinema hall view
        seats_list = request.POST.getlist('selected_seats')
        # creation of a random number used to fill reservation number
        random_int = randrange(1, 999999)

        # get repertoire instance for this specific screening
        repertoire = RepertoireModel.objects.get(pk=repertoire_id)

        # get all reservations for this specific screening
        reservations = ReservationModel.objects.filter(repertoire=repertoire)
        # get all booked seats
        booked_seats_list = get_booked_seats(reservation_instance=reservations)
        # checking if the places to be booked are not already booked - validation in case of data replacement in html
        try:
            for seat_to_be_booked in seats_list:
                # checking if the place selected by user is not already in the database as reserved
                # (for a given screening)
                if seat_to_be_booked in booked_seats_list:
                    raise ValidationError('This seat is already booked - it is in database!')
        except ValidationError as err:
            print('ERROR: ', repr(err), flush=True)
            return render(request, 'reservations_app/booking_failure.html')

        # Check for duplicate seats in the list - validation in case of data replacement in html
        try:
            # remove duplicates and compare list length
            if len(seats_list) != len(dict.fromkeys(seats_list)):
                raise ValidationError('Duplication of selected seats!')
        except ValidationError as err:
            print('ERROR: ', repr(err), flush=True)
            return render(request, 'reservations_app/booking_failure.html')

        # create reservation for this specific order (is not yet saved to database)
        reservation = ReservationModel(buyer=buyer, repertoire=repertoire,
                                       reservation_number=f'{buyer.id}-{repertoire.id}-{random_int}')

        # get instances of seats from database (SeatModel) and check if this seats exists in database - validation
        # if everything is ok (no errors) save reservation to database
        seat_instance_from_db_list = []
        try:
            for seat in seats_list:
                # get instances of selected seats by user
                seat_instance_from_db = SeatModel.objects.get(position__exact=seat)
                seat_instance_from_db_list.append(seat_instance_from_db)
        except ObjectDoesNotExist as err:
            # there is no seats with that name in database
            print('ERROR: ', repr(err), flush=True)
            return render(request, 'reservations_app/booking_failure.html')
        # save reservation to database (so far with no assigned seats)
        reservation.save()
        # assigning selected seats (after validation) to a given reservation
        for seat_instance in seat_instance_from_db_list:
            reservation.booked_seats.add(seat_instance)

        context = {
            'repertoire': repertoire,
            'seats_count': len(seats_list),  # number of tickets booked
            'seats': seats_list,
            'buyer': buyer,
        }
        return render(request, 'reservations_app/booking_success.html', context=context)

    if request.method == 'GET':
        # back to repertoire view if page is refreshed
        return redirect(reverse_lazy('reservations_app:repertoire_view'))
