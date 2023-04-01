from rest_framework import permissions


class IsModeratorAdminOwner(permissions.BasePermission):
    """Доступ модератору, админу или автору объекта (field "author")."""

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if (
            request.user.role in ('moderator', 'admin')
            or obj.author == request.user
        ):
            return True
        return False

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)