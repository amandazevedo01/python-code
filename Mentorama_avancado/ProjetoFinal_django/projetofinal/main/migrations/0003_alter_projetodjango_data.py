# Generated by Django 4.1 on 2022-12-28 11:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_projetodjango_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projetodjango',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 28, 22, 22, 44, 900317), verbose_name='Publicado em'),
        ),
    ]
