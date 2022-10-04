from rest_framework import serializers
from rest_framework import validators

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор модели User."""

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "bio",
            "role",
        )
        lookup_field = "username"
        read_only_field = ('role',)
