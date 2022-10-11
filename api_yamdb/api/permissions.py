from rest_framework import permissions

from reviews.models import User


class IsAdmin(permissions.BasePermission):
    """Администратор."""

    def has_permission(self, request, view):
        user = request.user
        return (
            user.is_authenticated
            and (
                user.is_superuser
                or user.role == User.ADMIN
            )
        )


class IsAdminOrReadOnly(permissions.BasePermission):
    """Администратор или только для чтения."""

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.role == User.ADMIN
            or request.user.is_superuser
        )


class IsAuthorAdminModeratorOrReadOnly(permissions.BasePermission):
    """Администратор, модератор, автор или только для чтения."""

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.role == User.ADMIN
            or request.user.role == User.MODERATOR
            or request.user.is_superuser
            or obj.author == request.user
        )
