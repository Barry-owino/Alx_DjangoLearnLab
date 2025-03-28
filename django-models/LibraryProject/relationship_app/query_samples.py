import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

#query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name).first()
    if author:
        books = Book.objects.filter(author=author)

        if books.exist():
            for book in books:
                print(book.title)
         else:

              print(f"No book found for author: {author_name}")
    else:
        print(f"Author {author_name} not found.")


#list all books in a library
def get_books_in_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library:
        books = library.books.all()
        return [book.title for book in books]
    return []

def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name).first()
    if library and hasattr(library, "librarian"):
        return library.librarian.name
    return None

#example usage
if __name__ == "__main__":
    print(get_books_by_author("J.K. Rawlings"))
    print(get_books_in_library("Central Library"))
    print(get_librarian_for_library("Central Library"))


