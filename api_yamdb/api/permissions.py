from rest_framework import permissions

from titles.models import User


class IsAuthorOrReadOnlyPermission(permissions.BasePermission):
    """Автор или только для чтения."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.author == request.user


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


class IsAdminModeratorAuthor(permissions.BasePermission):
    """Администратор."""

    def has_object_permission(self, request, view, obj):
        user = request.user
        return (
            user.is_authenticated
            and (
                user.is_superuser
                or user.role == User.ADMIN
                or user.role == User.MODERATOR
                or obj.author == user
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
                and user.role == User.ADMIN or
                user.is_superuser
            )
        )


class IsAdminModeratorOrReadOnly(permissions.BasePermission):
    """Администратор или только для чтения."""

    def has_permission(self, request, view):
        user = request.user
        return (
            request.method in permissions.SAFE_METHODS
            or (
                user.is_authenticated
                and user.role == User.ADMIN or
                user.role == User.MODERATOR or
                user.is_superuser
            )
        )


class IsAuthorAdminModeratorOrReadOnly(permissions.BasePermission):
    """Администратор или только для чтения."""

    def has_object_permission(self, request, view, obj):
        user = request.user
        if (request.method in permissions.SAFE_METHODS or 
            user.is_authenticated and user.role == User.ADMIN or
            user.role == User.MODERATOR or user.is_superuser):
            return True
        return obj.author == request.user
