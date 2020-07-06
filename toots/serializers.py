from rest_framework import serializers
from django.conf import settings
from .models import Toot
from profiles.serializers import ProfileSerializer

MAX_LENGTH = settings.MAX_LENGTH
TOOT_ACTION_OPTIONS = settings.TOOT_ACTION_OPTIONS


class TootActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()
    content = serializers.CharField(allow_blank=True, required=False)

    def validate_action(self, value):
        value = value.lower().strip()
        if value not in TOOT_ACTION_OPTIONS:
            raise serializers.ValidationError("Invalid toot action!")
        return value


class TootCreateSerializer(serializers.ModelSerializer):
    user = ProfileSerializer(source="user.profile", read_only=True)
    likeCount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Toot
        fields = ["user", "id", "content", "likeCount"]

    def get_likeCount(self, obj):
        return obj.likes.count()

    def validate_content(self, value):
        if len(value) > MAX_LENGTH:
            raise serializers.ValidationError(
                "The toot is too long! The elephant is suffocating!"
            )

        if len(value) == 0:
            raise serializers.ValidationError("That is a silent toot!")

        return value

class TootSerializer(serializers.ModelSerializer):
    user = ProfileSerializer(source="user.profile", read_only=True)
    likeCount = serializers.SerializerMethodField(read_only=True)
    parent = TootCreateSerializer(read_only=True)

    class Meta:
        model = Toot
        fields = ["user", "id", "content", "likeCount", "is_retoot", "parent", "timestamp"]

    def get_likeCount(self, obj):
        return obj.likes.count()