from rest_framework import permissions

from users.models import UserRole


class IsCreatedByOrAdminOrModerator(permissions.BasePermission):
    message = 'Only user who created the ad, admin and moderators could modify or delete it.'

    def has_object_permission(self, request, view, obj):
        if request.user.role == UserRole.ADMIN or request.user.role == UserRole.MODERATOR:
            return True
        if obj.author == request.user:
            return True
        return False
