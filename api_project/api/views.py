# api/views.py

from rest_framework import generics , viewsets
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Get all books from the database
    serializer_class = BookSerializer  # Use the BookSerializer for JSON response

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Fetch all books
    serializer_class = BookSerializer  # Serialize Book model data
