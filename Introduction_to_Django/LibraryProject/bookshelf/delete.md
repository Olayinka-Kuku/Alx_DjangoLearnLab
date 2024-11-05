# Delete Operation

```python
# Import the Book model
from bookshelf.models import Book

# Command to delete the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
