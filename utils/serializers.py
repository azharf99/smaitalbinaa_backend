from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom token serializer to add extra user data to the JWT payload.
    """
    @classmethod
    def get_token(cls, user):
        # Get the default token payload
        token = super().get_token(user)

        # Add custom claims
        token['is_superuser'] = user.is_superuser

        return token