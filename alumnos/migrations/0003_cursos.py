# Generated by Django 4.1.3 on 2022-11-19 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0002_alter_alumnos_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('año', models.CharField(max_length=1)),
                ('division', models.CharField(max_length=1)),
            ],
        ),
    ]
