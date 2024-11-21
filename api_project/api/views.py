# api/views.py

from rest_framework import generics , viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Get all books from the database
    serializer_class = BookSerializer  # Use the BookSerializer for JSON response

# Added IsAuthenticated permission to the BookViewSet to restrict access to authenticated users
# This ensures that only authenticated users can perform actions on the 'Book' model data.
# The 'IsAuthenticated' permission class checks that the user is logged in before they can
# interact with the API.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Fetch all books
    serializer_class = BookSerializer  # Serialize Book model data
    permission_classes = [IsAuthenticated]  # Only authenticated users can access
