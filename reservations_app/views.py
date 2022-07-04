import operator
from datetime import date
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
        movies_list = []
        calendar_error = ''
        date_selected = request.GET.get('date')
        if date_selected is None:
            # view today's repertoire
            date_selected = date.today().strftime('%Y-%m-%d')
        # view selected repertoire
        # if wrong or no date selected - validation
        try:
            # get repertoire for a given day with no duplication of titles
            repertoire = RepertoireModel.objects.filter(screening_date=date_selected).distinct('movie')
            # to sort alphabetically
            # repertoire = RepertoireModel.objects.filter(id__in=repertoire).order_by('movie__title')
            for movie in repertoire:
                # get list of movies with the same title for a given day
                movies_by_title = RepertoireModel.objects.filter(movie__title=movie.movie.title, screening_date=date_selected)
                movies_list.append(movies_by_title)
            print('MOVIES LIST: ', movies_list, flush=True)
        except ValidationError as e:
            repertoire = RepertoireModel.objects.filter(screening_date=date.today()).order_by('screening_time')
            calendar_error = str(e)[5:71].capitalize()
        context = {
            'date_selected': date_selected,
            'calendar_error': calendar_error,
            'movies_list': movies_list,
        }
        return render(request, 'reservations_app/repertoire.html', context=context)
