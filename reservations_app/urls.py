from django.urls import path

from . import views

app_name = 'reservations_app'

urlpatterns = [
    path('', views.repertoire_view, name='home_view'),
    path('repertoire/', views.repertoire_view, name='repertoire_view'),
]
