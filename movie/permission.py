from rest_framework import permissions


class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if (
            request.method == "GET"
            or request.method == "POST"
            and request.user.is_superuser
            or request.method == "PATCH"
            and request.user.is_superuser
            or request.method == "DELETE"
            and request.user.is_superuser
        ):
            return True

        return False
