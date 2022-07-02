from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator


class Author(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Movie(models.Model):
    title = models.CharField(max_length=50, blank=False, unique=True)
    release_date = models.IntegerField(blank=False, null=False, default=2000, validators=[MinValueValidator(1800)])
    author = models.ForeignKey('Author', on_delete=models.PROTECT)
    duration = models.DurationField(blank=False)
    age_restrictions = models.IntegerField(null=True, blank=True,
                                           validators=[MinValueValidator(0), MaxValueValidator(99)])
    description = models.TextField(blank=True, null=True, validators=[MaxLengthValidator(2000)])

    def __str__(self):
        return self.title
