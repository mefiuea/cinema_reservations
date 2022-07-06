import operator
from datetime import date

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError

from .models import RepertoireModel


def home_view(request):
    return redirect(reverse_lazy('reservations_app:repertoire_view'))


def repertoire_view(request):
    if request.method == 'POST':
        pass

    if request.method == 'GET':
        genres_list = []
        calendar_error = ''
        date_selected = request.GET.get('date')
        if date_selected is None or date_selected == '':
            # view today's repertoire
            date_selected = date.today().strftime('%Y-%m-%d')
        # get repertoire for a given day
        repertoires = RepertoireModel.objects.filter(screening_date=date_selected).order_by('screening_time')
        # to sort alphabetically
        # repertoire = RepertoireModel.objects.filter(id__in=repertoire).order_by('movie__title')
        # to sort by price
        # repertoire = RepertoireModel.objects.filter(id__in=repertoire).order_by('price')

        # for repertoire in repertoires:
        #     print('SCREENING TIME: ', repertoire.screening_time, type(repertoire.screening_time), flush=True)

        # get genres of movies for specific repertoire
        for repertoire in repertoires:
            for genre in repertoire.movie.genre.all():
                genres_list.append((genre.genre, genre.id))

        # remove duplications from list
        genres_list = list(dict.fromkeys(genres_list))

        context = {
            'date_selected': date_selected,
            'calendar_error': calendar_error,
            'repertoires': repertoires,
            'genres': genres_list,
        }
        return render(request, 'reservations_app/repertoire.html', context=context)


def get_repertoire_by_selected_sorting(request):
    selected_sorting = request.GET.get('sorting_by')
    selected_date = request.GET.get('date')
    selected_genre = request.GET.get('genre')
    # validation for date
    if selected_date is None or selected_date == '':
        # view today's repertoire
        selected_date = date.today().strftime('%Y-%m-%d')
    print('SELECTED SORTING JAVA SCRIPT: ', selected_sorting, flush=True)
    print('SELECTED DATE JAVA SCRIPT: ', selected_date, flush=True)
    print('SELECTED GENRE JAVA SCRIPT: ', selected_genre, flush=True)
    # validation for sorting
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

    if selected_genre == 'no_filter':
        # use genre filter
        print('TUU!!!')
        repertoires = RepertoireModel.objects.filter(screening_date=selected_date).order_by(order_by)
    else:
        repertoires = RepertoireModel.objects.filter(screening_date=selected_date,
                                                     movie__genre=selected_genre).order_by(order_by)
    print('REPERTOIRES JAVA SCRIPT: ', repertoires, flush=True)

    context = {
        'repertoires': repertoires,
    }

    return render(request, 'reservations_app/repertoires_list_by_query_string.html', context=context)


def booking_view(request, repertoire_id):
    if request.method == 'POST':
        pass

    if request.method == 'GET':
        repertoire_id = repertoire_id
        repertoire = RepertoireModel.objects.get(pk=repertoire_id)

        context = {
            'repertoire_id': repertoire_id,
            'repertoire': repertoire,
        }
        return render(request, 'reservations_app/booking.html', context=context)


def booking_completed_view(request, repertoire_id):
    if request.method == 'POST':
        return render(request, 'reservations_app/booking_success.html')

    if request.method == 'GET':
        return redirect(reverse_lazy('reservations_app:repertoire_view'))
