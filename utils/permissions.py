from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to only allow admin users to edit objects.
    Read-only access is allowed for any request (authenticated or not).
    """

    def has_permission(self, request, view):
        # Allow read-only access for any request (GET, HEAD, OPTIONS)
        if request.method in SAFE_METHODS:
            return True

        # Write permissions are only allowed to admin users.
        return request.user and request.user.is_staff


class HasModelPermission(BasePermission):
    """
    Custom permission to only allow users with model permissions to edit objects.
    Read-only access is allowed for any request (authenticated or not).
    """

    # A mapping of request methods to the required permission codes.
    # 'view' permission is not checked for read-only access.
    perms_map = {
        'GET': [],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def has_permission(self, request, view):
        # Allow read-only access for any request.
        if request.method in SAFE_METHODS:
            return True

        # Check for user authentication for write permissions.
        if not request.user or not request.user.is_authenticated:
            return False

        # Get the model from the view's queryset.
        model = view.get_queryset().model
        app_label = model._meta.app_label
        model_name = model._meta.model_name
        perms = [perm % {'app_label': app_label, 'model_name': model_name} for perm in self.perms_map.get(request.method, [])]
        return request.user.has_perms(perms)