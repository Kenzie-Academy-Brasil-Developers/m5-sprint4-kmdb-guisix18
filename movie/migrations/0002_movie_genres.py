# Generated by Django 4.0.5 on 2022-06-28 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genre', '0002_remove_genre_movies'),
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(related_name='genres', to='genre.genre'),
        ),
    ]
