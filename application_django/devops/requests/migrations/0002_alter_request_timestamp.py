# Generated by Django 4.2.1 on 2023-10-02 18:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='timestamp',
            field=models.DateField(verbose_name=datetime.datetime(2023, 10, 2, 18, 38, 19, 21394)),
        ),
    ]
