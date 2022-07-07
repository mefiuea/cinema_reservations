# Generated by Django 4.0.5 on 2022-07-07 10:00

import custom.picture_size
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations_app', '0005_seats_generator'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviemodel',
            name='movie_picture',
            field=models.ImageField(blank=True, null=True, upload_to='movies_images/', validators=[custom.picture_size.picture_size]),
        ),
    ]