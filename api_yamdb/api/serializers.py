import datetime as dt
import re

from rest_framework import serializers, validators

from titles.models import User, Category, Genre, Title, Review, Comment


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


class RegistrationSerializer(serializers.Serializer):
    """Сериализатор данных регистрации."""

    username = serializers.CharField(
        validators=(
            validators.UniqueValidator(
                queryset=User.objects.all(),
                message='Имя занято.'
            ),
        ),
        required=True,
    )

    email = serializers.EmailField(
        validators=(
            validators.UniqueValidator(
                queryset=User.objects.all(),
                message='Email уже зарегистрирован.'
            ),
        ),
        required=True,
    )

    def validate_username(self, value):
        """Валидация поля username."""

        if value.lower() == 'me':
            raise serializers.ValidationError(
                "Имя зарезервировано."
            )

        if not re.match(r'^[\w.@+-]+\Z', value):  # шаблон из задания, может \Z
            #  r'^[\w.@+-]+)$' # шаблон из примеров
            #  r'^users/(?P<username>[\w.@+-]+)$' # шаблон для username
            raise serializers.ValidationError(
                "Неверный формат имени."
            )

        return value


class AuthetificationSerializer(serializers.Serializer):
    """Сериализатор данных аутентификации."""

    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)


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

    # Нельзя добавлять произведения, которые еще не вышли
    # (год выпуска не может быть больше текущего)
    def validate_year(self, value):
        year = dt.date.today().year
        if not value > year:
            raise serializers.ValidationError('Проверьте год поблукации!')
        return value


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Review
        read_only_fields = ('title',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('review',)
