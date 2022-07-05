from django.urls import path

from . import views

app_name = 'reservations_app'

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('repertoire/', views.repertoire_view, name='repertoire_view'),
    path('repertoire/get_repertoire_by_selected_sorting/', views.get_repertoire_by_selected_sorting,
         name='get_repertoire_by_selected_sorting_view'),
    path('repertoire/booking/<int:repertoire_id>/', views.booking_view, name='booking_view'),
]
