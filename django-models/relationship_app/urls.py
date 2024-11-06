from django.urls import path
from .views import list_books, LibraryDetailView, views, LoginView, LogoutView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register, name='register'),  # Registration page
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # Login page
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # Logout page
]
