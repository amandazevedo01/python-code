# Generated by Django 4.1 on 2023-01-02 10:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_projetodjango_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projetodjango',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 2, 21, 20, 50, 22191), verbose_name='Publicado em'),
        ),
    ]
