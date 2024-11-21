# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

# Initialize the router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')  # Register ViewSet

# Added /api-token-auth/ endpoint for token retrieval
# This endpoint allows users to obtain an authentication token by providing their username
# and password. The token can be used for authenticating future requests to the API.
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # API endpoint for listing books
    path('', include(router.urls)),  # Include the router's URLs for CRUD operations
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

