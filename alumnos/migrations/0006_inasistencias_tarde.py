# Generated by Django 4.1.3 on 2022-11-20 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0005_alumnos_curso'),
    ]

    operations = [
        migrations.AddField(
            model_name='inasistencias',
            name='tarde',
            field=models.BooleanField(default=False),
        ),
    ]
