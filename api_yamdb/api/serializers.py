import datetime as dt

from rest_framework import serializers

from .models import User, Category, Genre, Title


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


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Category


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        read_only=True, slug_field='???'
    )
    category = serializers.SlugRelatedField(
        read_only=True, slug_field='???'
    )

    class Meta:
        fields = '__all__'
        model = Title

    # Нельзя добавлять произведения, которые еще не вышли (год выпуска не может быть больше текущего)
    def validate_year(self, value):
        year = dt.date.today().year
        if not value > year:
            raise serializers.ValidationError('Проверьте год поблукации!')
        return value
