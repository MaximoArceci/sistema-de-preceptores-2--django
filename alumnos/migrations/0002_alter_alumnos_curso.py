# Generated by Django 4.1.3 on 2022-11-12 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='curso',
            field=models.CharField(choices=[('5A', "Quinto año 'A'"), ('5B', "Quinto año 'B'"), ('4A', "Cuarto año 'A'"), ('4B', "Cuarto año 'B'"), ('3A', "Tercero año 'A'"), ('3B', "Tercero año 'B'"), ('2A', "Segundo año 'A'"), ('2B', "Segundo año 'B'"), ('1A', "Primero año 'A'"), ('1B', "Primero año 'B'")], max_length=2),
        ),
    ]
