from rest_framework import serializers
from .models import Message


class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["text"]

    def create(self, validated_data):
        return Message.objects.create(
            sender="user",
            text=validated_data["text"]
        )


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["id", "sender", "text", "created_at"]
