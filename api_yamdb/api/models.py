from email.policy import default
from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


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
        default="",
        editable=False,
        unique=True,
        blank=True, null=True,
    )

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
