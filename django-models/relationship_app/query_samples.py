# query_samples.py

from relationship_app.models import Author, Librarian, Library, Book

# Function to retrieve all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)  # Get the author by name
        books = Book.objects.filter(author=author)  # Filter books by the author
        return books
    except Author.DoesNotExist:
        return None

# Function to retrieve the librarian for a specific library
def get_librarian_for_library(library_id):
    try:
        librarian = Librarian.objects.get(library_id=library_id)
        return librarian
    except Librarian.DoesNotExist:
        return None

# Function to list all books in a specific library
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # Gets all books related to the library
        return books
    except Library.DoesNotExist:
        return None

# Example usage:
if __name__ == "__main__":
    author_name = "Author Name"  # Change this to the name of the author you want to check
    books_by_author = get_books_by_author(author_name)
    if books_by_author:
        print(f"Books by {author_name}:")
        for book in books_by_author:
            print(f"- {book.title}")
    else:
        print(f"There are no books by {author_name} or the author does not exist.")

    library_name = "My Library"  # Change this to the name of the library you want to check
    librarian = get_librarian_for_library(1)  # Change this if needed
    if librarian:
        print(f"The librarian for {library_name} is {librarian.name}.")
    else:
        print(f"There is no librarian for {library_name}.")

    # List all books in the specified library
    books = list_books_in_library(library_name)
    if books:
        print(f"Books in {library_name}:")
        for book in books:
            print(f"- {book.title}")
    else:
        print(f"There are no books in {library_name} or the library does not exist.")
