from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator

from custom.picture_size import picture_size


class AuthorModel(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class MovieGenresModel(models.Model):
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.genre


class MovieModel(models.Model):
    title = models.CharField(max_length=50, blank=False, unique=True)
    release_date = models.IntegerField(blank=False, null=False, default=2000, validators=[MinValueValidator(1800)])
    author = models.ForeignKey('AuthorModel', on_delete=models.PROTECT)
    duration = models.DurationField(blank=False)
    age_restrictions = models.IntegerField(null=True, blank=True,
                                           validators=[MinValueValidator(0), MaxValueValidator(99)])
    description = models.TextField(blank=True, null=True, validators=[MaxLengthValidator(2000)])
    genre = models.ManyToManyField('MovieGenresModel', related_name='movie_genre')
    movie_picture = models.ImageField(upload_to='movies_images/', blank=True, null=True, validators=[picture_size])

    def __str__(self):
        return self.title


class CinemaHallModel(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)
    size = models.IntegerField(blank=False, null=True, validators=[MinValueValidator(0), MaxValueValidator(5000)])

    def __str__(self):
        return self.name


class RepertoireModel(models.Model):
    movie = models.ForeignKey('MovieModel', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=5, decimal_places=2,
                                validators=[MinValueValidator(0), MaxValueValidator(1000)], default=30.00)
    screening_date = models.DateField()
    screening_time = models.TimeField()
    cinema_hall = models.ForeignKey('CinemaHallModel', on_delete=models.PROTECT)

    def __str__(self):
        return f'Repertoire: {self.id}, {self.movie}, {self.screening_date}, {self.screening_time}'


class SeatModel(models.Model):
    position = models.CharField(max_length=4)

    def __str__(self):
        return self.position


class ReservationModel(models.Model):
    buyer = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    repertoire = models.ForeignKey('RepertoireModel', on_delete=models.PROTECT)
    booked_seats = models.ManyToManyField('SeatModel', related_name='reservation_seat')
    reservation_number = models.CharField(max_length=255)

    def __str__(self):
        return f'Reservation: {self.id}, {self.buyer}, {self.repertoire}, {self.booked_seats}'
