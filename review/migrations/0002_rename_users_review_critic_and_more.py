# Generated by Django 4.0.5 on 2022-07-01 01:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='users',
            new_name='critic',
        ),
        migrations.AlterField(
            model_name='review',
            name='recomendation',
            field=models.CharField(choices=[('MW', 'Must Watch'), ('SW', 'Should Watch'), ('AW', 'Avoit Watch'), ('NO', 'No opinion')], default='NO', max_length=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]
