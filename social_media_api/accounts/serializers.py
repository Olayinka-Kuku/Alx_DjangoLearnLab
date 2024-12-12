from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

# Assuming you are using a custom user model
User = get_user_model()

# Serializer for User Registration
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']  # Add other fields if necessary

    def create(self, validated_data):
        # Create a new user with the validated data
        user = User.objects.create_user(**validated_data)
        return user

# Serializer for User Login (Optional, if you need login-related serialization)
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

# Serializer for User Profile (Fetching user data)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']  # Add other profile fields if necessary

