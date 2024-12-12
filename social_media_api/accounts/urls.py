from django.urls import path, include
from .views import RegisterView
from django.contrib import admin



urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
]
