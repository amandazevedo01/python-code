# Generated by Django 4.1.1 on 2022-09-08 22:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projetodjango',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 8, 19, 51, 38, 686282), verbose_name='Publicado em'),
        ),
    ]
