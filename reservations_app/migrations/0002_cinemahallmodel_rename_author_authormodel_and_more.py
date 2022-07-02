# Generated by Django 4.0.5 on 2022-07-02 16:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CinemaHallModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('size', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5000)])),
            ],
        ),
        migrations.RenameModel(
            old_name='Author',
            new_name='AuthorModel',
        ),
        migrations.RenameModel(
            old_name='Movie',
            new_name='MovieModel',
        ),
        migrations.CreateModel(
            name='RepertoireModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=30.0, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)])),
                ('screening_date', models.DateField()),
                ('screening_time', models.TimeField()),
                ('cinema_hall', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reservations_app.cinemahallmodel')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reservations_app.moviemodel')),
            ],
        ),
    ]