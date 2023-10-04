# Generated by Django 4.2.1 on 2023-10-02 18:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipv4_address', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=100)),
                ('timestamp', models.DateField(verbose_name=datetime.datetime(2023, 10, 2, 18, 31, 26, 890840))),
                ('http_method', models.CharField(max_length=25)),
                ('content', models.CharField(max_length=10)),
            ],
        ),
    ]
