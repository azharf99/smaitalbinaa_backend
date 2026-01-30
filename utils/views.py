from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import MyTokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth import logout

class MyTokenObtainPairView(TokenObtainPairView):
    """
    Custom view to use the custom token serializer.
    """
    serializer_class = MyTokenObtainPairSerializer


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            # Delete the user's token to log them out
            request.user.auth_token.delete()
            logout(request)
            return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
        except AttributeError:
            try:
                refresh_token = request.data["refresh"]
                token = RefreshToken(refresh_token)
                token.blacklist()
                logout(request)
                return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
            except Exception as e:
                logout(request)
        return Response({"message": "Logged out successfully."}, status=status.HTTP_200_OK)