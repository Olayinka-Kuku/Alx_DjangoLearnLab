# query_samples.py

from relationship_app.models import Librarian, Library

# Retrieve the librarian for a specific library
def get_librarian_for_library(library_id):
    try:
        librarian = Librarian.objects.get(library_id=library_id)
        return librarian
    except Librarian.DoesNotExist:
        return None

# Example usage:
if __name__ == "__main__":
    library_id = 1  # Change this to the ID of the library you want to check
    librarian = get_librarian_for_library(library_id)
    if librarian:
        print(f"The librarian for library ID {library_id} is {librarian.name}.")
    else:
        print(f"There is no librarian for library ID {library_id}.")
