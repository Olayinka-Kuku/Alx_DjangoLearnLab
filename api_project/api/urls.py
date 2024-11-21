# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Initialize the router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')  # Register ViewSet

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # API endpoint for listing books
     path('', include(router.urls)),  # Include the router's URLs for CRUD operations
]
