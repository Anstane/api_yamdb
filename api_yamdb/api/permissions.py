from rest_framework import permissions

from .models import User


class IsAuthorOrReadOnlyPermission(permissions.BasePermission):
    """Автор или только для чтения."""

    def has_object_permission(self, request, view, obj):
        return any((
            request.method in permissions.SAFE_METHODS,
            request.user == obj,
        ))
