# Generated by Django 2.2.4 on 2019-09-23 15:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='data_cadastro',
            field=models.DateTimeField(default=datetime(2019, 9, 23, 15, 53, 38, 741341)),
        ),
    ]
