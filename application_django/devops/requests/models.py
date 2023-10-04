from django.db import models
from datetime import datetime
# Create your models here.


class Request(models.Model):
    ipv4_address = models.CharField(max_length=15)
    name = models.CharField(max_length=100)
    timestamp = models.CharField(max_length=200)
    http_method = models.CharField(max_length=25)
    message = models.CharField(max_length=1000)