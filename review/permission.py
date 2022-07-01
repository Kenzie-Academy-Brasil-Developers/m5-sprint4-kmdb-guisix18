from rest_framework import permissions


class AuthReview(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated or request.method in permissions.SAFE_METHODS:
            return True
        return False


class AuthDeleteReview(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.critic == request.user or request.user.is_superuser:
            return True
        return False
