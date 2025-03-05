from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic import CreateView

from .decorators import role_required

#from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Book
from .models import Library
#from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

@role_required('Admin')
def admin_dashboard(request):
    return render(request, 'relationship_app/admin_dashboard.html')

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



def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

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
