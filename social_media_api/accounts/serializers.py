from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Get the User model
User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    # Using serializers.CharField() for password field
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        # Using get_user_model().objects.create_user to create a new user
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', '')
        )
        # Create a token for the new user
        Token.objects.create(user=user)
        return user
