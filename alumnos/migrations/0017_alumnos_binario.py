# Generated by Django 4.1.3 on 2023-01-02 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0016_alter_alumnos_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnos',
            name='binario',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]
