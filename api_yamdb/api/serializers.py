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
        lookup_field = 'username'
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }
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
        fields = ('name', 'slug',)
        model = Category
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'slug',)
        model = Genre
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class TitleReadSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        fields = (
            'id', 'name', 'year', 'rating', 'description', 'genre', 'category',
        )
        model = Title


class TitleWriteSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        slug_field='genre',
        queryset=Genre.objects.all(),
        many=True
    )
    category = serializers.SlugRelatedField(
        slug_field='category',
        queryset=Category.objects.all()
    )

    class Meta:
        fields = ('name', 'year', 'description', 'genre', 'category',)
        model = Title

    def validate_year(self, value):
        year = dt.date.today().year
        if value > year:
            raise serializers.ValidationError('Проверьте год поблукации!')
        return value


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        fields = ('id', 'text', 'score', 'author', 'pub_date',)
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date',)
        model = Comment
