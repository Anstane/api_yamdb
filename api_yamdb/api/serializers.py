from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор модели User."""

    # ^[\w.@+-]+\z
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


