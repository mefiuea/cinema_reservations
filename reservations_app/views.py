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
        calendar_error = ''
        date_selected = request.GET.get('date')
        if date_selected is None:
            # view today's repertoire
            date_selected = date.today().strftime('%Y-%m-%d')
            print('TODAY: ', date_selected, flush=True)
            repertoire = RepertoireModel.objects.filter(screening_date=date.today())
        else:
            # view selected repertoire
            # if wrong or no date selected - validation
            try:
                repertoire = RepertoireModel.objects.filter(screening_date=date_selected)
            except ValidationError as e:
                repertoire = RepertoireModel.objects.filter(screening_date=date.today())
                calendar_error = str(e)[5:71].capitalize()
                print('ERROR: ', calendar_error, type(calendar_error), flush=True)
        print('REPERTOIRE: ', repertoire, flush=True)
        context = {
            'repertoire': repertoire,
            'date_selected': date_selected,
            'calendar_error': calendar_error,
        }
        return render(request, 'reservations_app/repertoire.html', context=context)
