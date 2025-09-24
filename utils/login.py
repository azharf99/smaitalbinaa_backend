from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import urllib.parse

@login_required
def exchange_token(request):
    # This view is hit after the user has successfully logged in via social auth
    # The `request.user` is now populated by the social_django backend.
    
    # Generate a JWT for the user
    refresh = RefreshToken.for_user(request.user)
    access_token = str(refresh.access_token)
    refresh_token = str(refresh)

    # URL encode the tokens to safely pass them as query parameters
    params = urllib.parse.urlencode({
        'access': access_token,
        'refresh': refresh_token,
    })
    
    # Redirect back to the React app with the tokens in the URL
    # In a real production app, you might use a more secure method
    # like setting HttpOnly cookies.
    return redirect(f'http://localhost:5173/social-auth-callback?{params}')
