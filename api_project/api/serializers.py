# api/serializers.py

from rest_framework import serializers
from .models import Book  # Ensure this imports your Book model

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book  # The model this serializer represents
        fields = '__all__'  # Include all fields from the Book model
