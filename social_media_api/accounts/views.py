from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, get_user_model
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer, CustomUserSerializer
from django.contrib.auth import login
from rest_framework.decorators import api_view, permission_classes
from .models import CustomUser


# User Registration View
class UserRegistrationView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = RegisterSerializer

# Login View
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # Log the user in
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Profile View
class UserProfileView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

# Example for following a user
@api_view(['POST'])
def follow_user(request, user_id):
    if not request.user.is_authenticated:
        return Response({"detail": "Authentication credentials were not provided."}, status=401)

    try:
        user_to_follow = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        return Response({"detail": "User not found."}, status=404)

    # Add the user to the follow list
    request.user.following.add(user_to_follow)
    return Response({"detail": "Followed successfully."}, status=200)

# Example for unfollowing a user
@api_view(['POST'])
def unfollow_user(request, user_id):
    if not request.user.is_authenticated:
        return Response({"detail": "Authentication credentials were not provided."}, status=401)

    try:
        user_to_unfollow = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        return Response({"detail": "User not found."}, status=404)

    # Remove the user from the follow list
    request.user.following.remove(user_to_unfollow)
    return Response({"detail": "Unfollowed successfully."}, status=200)

# Example to list all users to follow
@api_view(['GET'])
def list_users(request):
    if not request.user.is_authenticated:
        return Response({"detail": "Authentication credentials were not provided."}, status=401)

    users = CustomUser.objects.all()  # Fetch all users
    serializer = CustomUserSerializer(users, many=True)
    return Response(serializer.data)
