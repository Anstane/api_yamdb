from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from reviews.models import User


class UserAdmin(admin.ModelAdmin):
    """Класс администрирования модели User."""

    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'bio',
        'role',
    )

    list_filter = (
        'role',
    )

    search_fields = (
        'username',
        'email',
        'last_name',
    )


admin.site.register(User, UserAdmin)
