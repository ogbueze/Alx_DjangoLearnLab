import os
import django

# --------------------------------------------------
# Django environment setup
# --------------------------------------------------
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'library_project.settings'
)
django.setup()

# --------------------------------------------------
# Model imports
# --------------------------------------------------
from relationship_app.models import (
    Author,
    Book,
    Library,
    Librarian
)

# --------------------------------------------------
# Queries
# --------------------------------------------------

def query_books_by_author(author_name):
    # Query all books by a specific author
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books


def list_books_in_library(library_name):
    """
    List all books in a library
    """
    library = Library.objects.get(name=library_name)
    books = library.book_set.all()  # or library.books.all() if related_name is set
    return books


def get_librarian_for_library(library_name):
    # Retrieve the librarian for a library
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian


# --------------------------------------------------
# Optional test execution
# --------------------------------------------------
if __name__ == "__main__":
    print("Books by Author:")
    for book in query_books_by_author("Chinua Achebe"):
        print(book.title)

    print("\nBooks in Library:")
    for book in list_books_in_library("Central Library"):
        print(book.title)

    print("\nLibrarian:")
    librarian = get_librarian_for_library("Central Library")
    print(librarian.name)
