from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from django.views.generic import CreateView

from .decorators import role_required

from django.http import HttpResponseRedirect
from django.urls import reverse

#import { render, redirect } from 'django-shortcuts';
#from { login_required, permissions_required } from 'django-contrib-auth-decorators';


#from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Book
from .models import Library

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib import messages

from .forms import BookForm
#from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

"""
@login_required
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.created_by = request.user
            book.save()
            messages.success(request, 'Book added successfully.')
            return redirect('book_list')
    else:
        form = BookForm()
return render(request, 'add_book.html', {'form': form})
"""
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        pass
    return render(request, 'add_book.html')

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # Handle form submission to edit the book
        pass
    return render(request, 'edit_book.html', {'book': book})

# Delete Book view
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to the book list page
    return render(request, 'delete_book.html', {'book': book})

# List Books view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})




#end of updates

@role_required('Admin')
def admin_view(request):
    return render(request, 'admin_dashboard.html')

@role_required('Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_dashboard.html')

@role_required('Member')
def member_view(request):
    return render(request, 'relationship_app/member_dashboard.html')

def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@login_required
@user_passes_test(is_admin, login_url='/login/')
def admin_view(request):
    return render(request, 'admin_dashboard.html')
"""
#custom permissions
@login_required
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
   return render(request, 'edit_book.html', {'form': form})

"""                  
"""
@login_required
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    return redirect('book_list')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')

    else:
       form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
"""
"""
@login_required
#need to cumback and list_books/book_list/this error neeed to fixed
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})
"""
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = '/login/'

class CustomLogoutView(LogoutView):
    template_name = 'registration/logout.html'
