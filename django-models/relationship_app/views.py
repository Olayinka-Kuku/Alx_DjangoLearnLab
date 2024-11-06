from django.shortcuts import render
from .models import Book,Library
from .models import Library
from django.views.generic.detail import DetailView

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})  # Render the template with books

# Class-based view for library details
class LibraryDetailView(DetailView):
    def get(self, request, pk):
        library = Library.objects.get(pk=pk)  # Fetch library by primary key
        return render(request, 'relationship_app/library_detail.html', {'library': library})  # Render the template with library details

# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'