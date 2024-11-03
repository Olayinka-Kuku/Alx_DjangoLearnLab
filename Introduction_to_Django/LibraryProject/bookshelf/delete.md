# Delete Operation

**Command:**
```python
retrieved_book.delete()
Book.objects.all()  # To confirm deletion, this should return an empty QuerySet


Expected Output: QuerySet []>
This confirms the book was deleted from the database.