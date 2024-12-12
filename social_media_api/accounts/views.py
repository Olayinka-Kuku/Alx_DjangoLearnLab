from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, get_user_model
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from django.contrib.auth import login

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
