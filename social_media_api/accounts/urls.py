from django.urls import path
from .views import UserRegistrationView, LoginView, UserProfileView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),  # Registration route
    path('login/', LoginView.as_view(), name='login'),                  # Login route
    path('profile/', UserProfileView.as_view(), name='profile'),        # Profile management route
]
