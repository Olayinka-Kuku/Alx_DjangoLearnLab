# Create Operation

**Command:**
```python
from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()


Expected Output: No direct output, but the book instance is saved in the database.