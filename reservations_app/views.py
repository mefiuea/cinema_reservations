from django.shortcuts import render, redirect
from django.urls import reverse_lazy


def home_view(request):
    return redirect(reverse_lazy('reservations_app:repertoire_view'))


def repertoire_view(request):
    if request.method == 'POST':
        pass

    if request.method == 'GET':
        return render(request, 'reservations_app/repertoire.html')
