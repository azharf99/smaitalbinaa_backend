import threading

from django.http import HttpRequest, HttpResponse

# Thread-local storage to hold the current user
_user = threading.local()

class CurrentUserMiddleware:
    """Middleware to store the currently logged-in user in thread-local storage."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Store the user for this request
        _user.value = request.user

        # Process the request/response cycle
        response = self.get_response(request)

        # Cleanup after request is finished
        _user.value = None
        return response



def get_current_user():
    """Return the user stored in thread-local storage."""
    return getattr(_user, "value", None)



class SetCurrentUserMixin:
    """
    Mixin to set the current user in thread-local storage for DRF views.
    """
    def initial(self, request, *args, **kwargs):
        _user.value = request.user
        super().initial(request, *args, **kwargs)



class NormalizePathMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        # Remove leading slashes from the path
        request.path_info = '/' + request.path_info.lstrip('/')
        return self.get_response(request)