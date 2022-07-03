from django.contrib import admin

from .models import AuthorModel, MovieModel, CinemaHallModel, RepertoireModel, SeatModel, ReservationModel, \
    MovieGenresModel


@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(MovieModel)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'duration')


@admin.register(CinemaHallModel)
class CinemaHallAdmin(admin.ModelAdmin):
    list_display = ('name', 'size')


@admin.register(RepertoireModel)
class RepertoireAdmin(admin.ModelAdmin):
    list_display = ('movie', 'cinema_hall', 'screening_date', 'screening_time')


@admin.register(SeatModel)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('position',)


@admin.register(ReservationModel)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'repertoire', 'reservation_number')


@admin.register(MovieGenresModel)
class MovieGenresAdmin(admin.ModelAdmin):
    list_display = ('genre',)
