from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view
    list_display = ('title', 'author', 'publication_year')
    # Add a filter sidebar to filter by publication_year
    list_filter = ('publication_year',)
    # Enable search functionality for title and author fields
    search_fields = ('title', 'author')

# Register the Book model with the custom admin settings
admin.site.register(Book, BookAdmin)
