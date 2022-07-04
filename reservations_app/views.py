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
        movies_list = []
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

        context = {
            'date_selected': date_selected,
            'calendar_error': calendar_error,
            'repertoires': repertoires,
        }
        return render(request, 'reservations_app/repertoire.html', context=context)


def get_repertoire_by_selected_sorting(request):
    selected_sorting = request.GET.get('sorting_by')
    selected_date = request.GET.get('date')
    if selected_date is None or selected_date == '':
        # view today's repertoire
        selected_date = date.today().strftime('%Y-%m-%d')
    print('SELECTED SORTING JAVA SCRIPT: ', selected_sorting, flush=True)
    print('SELECTED DATE JAVA SCRIPT: ', selected_date, flush=True)
    if selected_sorting == 'screening_time':
        order_by = 'screening_time'
    elif selected_sorting == 'alphabetically':
        order_by = 'movie__title'
    elif selected_sorting == 'duration':
        order_by = 'movie__duration'
    else:
        order_by = 'screening_time'
    repertoires = RepertoireModel.objects.filter(screening_date=selected_date).order_by(order_by)
    print('REPERTOIRES JAVA SCRIPT: ', repertoires, flush=True)

    context = {
        'repertoires': repertoires,
    }

    return render(request, 'reservations_app/repertoires_list_by_query_string.html', context=context)
