# Generated by Django 4.2.1 on 2023-10-03 09:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0004_alter_request_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='timestamp',
            field=models.DateField(verbose_name=datetime.datetime(2023, 10, 3, 9, 2, 37, 725387)),
        ),
    ]
