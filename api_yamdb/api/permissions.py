from rest_framework import permissions

from titles.models import User


class IsAuthorOrReadOnlyPermission(permissions.BasePermission):
    """Автор или только для чтения."""

    def has_object_permission(self, request, view, obj):
        return any((
            request.method in permissions.SAFE_METHODS,
            request.user == obj,
        ))

class IsAdmin(permissions.BasePermission):
    """Администратор."""

    def has_permission(self, request, view):
        return all((
            request.user.is_authenticated,
            request.user.role == User.ADMIN,
        ))


class IsAdminOrReadOnly(permissions.BasePermission):
    """Администратор или только для чтения."""

    def has_permission(self, request, view):
        user = request.user
        return any((
            request.method in permissions.SAFE_METHODS,
            all((
                user.is_authenticated,
                user.role == User.ADMIN,
            )),
        ))
