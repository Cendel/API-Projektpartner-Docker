from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    senderName = serializers.CharField(source='sender.name', read_only=True)
    senderEmail = serializers.CharField(source='sender.email', read_only=True)

    class Meta:
        model = Message
        fields = "__all__"


class MessageListSerializer(serializers.ModelSerializer):
    senderName = serializers.CharField(source='sender.name', read_only=True)

    class Meta:
        model = Message
        fields = ("id", "sender", "senderName", "title", "created_date")
