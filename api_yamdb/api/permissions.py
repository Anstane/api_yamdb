from rest_framework import permissions

from titles.models import User


class IsAuthorOrReadOnlyPermission(permissions.BasePermission):
    """Автор или только для чтения."""

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user == obj
        )


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
        user = request.user
        return (
            request.method in permissions.SAFE_METHODS
            or (
                user.is_authenticated
                and user.role == User.ADMIN
            )
        )
