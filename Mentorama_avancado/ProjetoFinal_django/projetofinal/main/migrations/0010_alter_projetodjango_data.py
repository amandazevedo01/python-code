# Generated by Django 4.1 on 2023-01-02 11:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_projetodjango_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projetodjango',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 2, 22, 23, 55, 885191), verbose_name='Publicado em'),
        ),
    ]
