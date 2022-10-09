from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from titles.models import User, Category, Genre, Title, Review, Comment


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
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Title)
admin.site.register(Review)
admin.site.register(Comment)
