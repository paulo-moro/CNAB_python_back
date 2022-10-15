from rest_framework import permissions


class IsAdminOrOwner(permissions.BasePermission):
    """Is Admin or Object owner permission"""

    def has_object_permission(self, request, view, obj):
  
        return request.user.is_superuser or obj == request.user
