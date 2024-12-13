from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token  # <-- Import Token model
from django.contrib.auth import authenticate
from .models import CustomUser  # Assuming you're using a custom user model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'date_of_birth', 'profile_photo')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        
        # Create token for the newly created user
        token = Token.objects.create(user=user)  # <-- Create a token for the user
        return user, token  # Return user and token

# Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user:
            return {'user': user}
        raise serializers.ValidationError("Invalid credentials")

# Token Serializer (for token retrieval)
class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key']
