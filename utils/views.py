from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    """
    Custom view to use the custom token serializer.
    """
    serializer_class = MyTokenObtainPairSerializer