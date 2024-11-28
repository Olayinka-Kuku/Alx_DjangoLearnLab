from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Book, Author
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class BookAPITests(APITestCase):
    def setUp(self):
        # Create test author
        self.author = Author.objects.create(name="Test Author")
        # Create test book
        self.book = Book.objects.create(title="Test Book", author=self.author, publication_year=2024)
        # Create a user and obtain a token for authentication
        self.user = User.objects.create_user(username="testuser", password="password")
        self.token = Token.objects.create(user=self.user)
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

    def test_create_book(self):
        url = reverse('book-list')  # Adjust according to your URL config
        data = {
            'title': 'New Book',
            'author': self.author.id,
            'publication_year': 2023
        }
        
        response = self.client.post(url, data, HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)


    def test_update_book(self):
        url = reverse('book-detail', args=[self.book.id])  # Adjust to match your URL pattern
        data = {
            'title': 'Updated Book Title',
            'author': self.author.id,
            'publication_year': 2025
        }
        response = self.client.put(url, data, HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book Title')

    def test_delete_book(self):
        url = reverse('book-detail', args=[self.book.id])  # Adjust to match your URL pattern
        response = self.client.delete(url, HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_list_books(self):
        url = reverse('book-list')  # Adjust to match your URL pattern
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_books_by_title(self):
        url = reverse('book-list') + '?title=Test'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_author(self):
        url = reverse('book-list') + '?search=Test Author'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_year(self):
        url = reverse('book-list') + '?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2024)  # Verify the ordering
