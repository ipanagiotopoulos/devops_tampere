# todo/todo_api/serializers.py
from rest_framework import serializers
from .models import Request


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ["ipv4_address", "name", "timestamp", "http_method", "message"]