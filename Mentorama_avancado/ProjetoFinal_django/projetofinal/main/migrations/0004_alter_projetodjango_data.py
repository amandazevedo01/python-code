# Generated by Django 4.1 on 2022-12-28 11:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_projetodjango_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projetodjango',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 28, 22, 23, 0, 706385), verbose_name='Publicado em'),
        ),
    ]
