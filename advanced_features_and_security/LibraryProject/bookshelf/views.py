from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

def book_list(request):
    # Fetch all books or a filtered set depending on your requirements
    books = Book.objects.all()  # Or use filters to customize
    return render(request, 'bookshelf/book_list.html', {'books': books})

from django.views.generic import ListView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'bookshelf/book_list.html'
    context_object_name = 'books'




@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        published_date = request.POST['published_date']
        Book.objects.create(title=title, author=author, published_date=published_date)
    return render(request, 'create_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.save()
    return render(request, 'edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return render(request, 'book_deleted.html')

