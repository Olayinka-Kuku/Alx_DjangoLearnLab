# query_samples.py

from relationship_app.models import Librarian, Library, Book

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
