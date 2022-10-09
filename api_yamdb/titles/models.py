import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """ Класс экземпляра пользователя."""

    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    ROLE_CHOICES = (
        (USER, 'Пользователь'),
        (MODERATOR, 'Модератор'),
        (ADMIN, 'Администратор')
    )

    username = models.CharField(
        'Логин',
        max_length=150,
        unique=True,
        blank=False, null=False,
    )
    email = models.EmailField(
        'Почта',
        max_length=254,
        unique=True,
        blank=False, null=False,
    )
    first_name = models.CharField(
        'Имя',
        max_length=150,
        blank=True, null=True,
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=150,
        blank=True, null=True,
    )
    bio = models.TextField(
        'Биография',
        blank=True, null=True,
    )
    role = models.CharField(
        'Роль',
        max_length=9,
        choices=ROLE_CHOICES,
        default=USER,
        blank=False, null=False,
    )
    confirmation_code = models.UUIDField(
        default=uuid.uuid4(),
        editable=False,
        unique=False,
    )

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

        constraints = (
            models.UniqueConstraint(
                fields=('username', 'confirmation_code',),
                name='unique_username_confirmation_code'
            ),
        )

    def __str__(self):
        return self.username


# Стоит ли нам обрезать метод __str__ по первым 15 символам?
class Category(models.Model):

    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name[:15]


class Genre(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name[:15]


class Title(models.Model):
    name = models.TextField()
    year = models.DateTimeField('Год публикации')
    description = models.TextField()
    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE, related_name='titles')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='titles')

    def __str__(self):
        return self.name[:15]


class Review(models.Model):
    text = models.TextField()
    score = models.IntegerField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews')
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True)

    class Meta:
        ordering = ['pub_date']
        constraints = [
            models.CheckConstraint(
                check=models.Q(score__gte=1) & models.Q(score__lt=10),
                name='Значение score от 1 до 10',
            )
        ]

    def __str__(self):
        return self.text[:15]


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments')
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.text[:15]
