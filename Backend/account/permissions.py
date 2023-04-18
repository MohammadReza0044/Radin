from rest_framework.permissions import BasePermission


class IsCEOOrIsAdministration(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_CEO
            or request.user
            and request.user.is_Administration_Manager
        )
