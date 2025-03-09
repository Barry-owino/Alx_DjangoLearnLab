from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .forms import ExampleForm
from .models import Book

#added the form to the views
def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the form data
            form.save()
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})

#search class
def search_books(request):
    search_term = request.GET.get("query", "")
    books = Book.objects.filter(Q(title__incontains=search_term))
    return render(request, "bookshelf/book_list.html", {"books": books})

@permission_required('bookshelf.com_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'book': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # Logic for creating a book (handle forms, validation, etc.)
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Logic for editing a book
    pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')

