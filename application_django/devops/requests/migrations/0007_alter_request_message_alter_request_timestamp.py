# Generated by Django 4.2.1 on 2023-10-03 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0006_rename_content_request_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='message',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='request',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
