from threading import local

_thread_locals = local()

def get_current_user():
    """
    Returns the user object for the current request.
    This is useful for accessing the user in places like signals.
    """
    return getattr(_thread_locals, 'user', None)