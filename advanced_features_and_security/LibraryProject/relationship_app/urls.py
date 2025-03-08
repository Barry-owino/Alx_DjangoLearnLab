from django.urls import path
from .views import list_books, LibraryDetailView
#from .views import login_view, RegisterView, CustomLogoutView
from .views import login_view, librarian_view, member_view
from django.urls import path

from .views import add_book, edit_book, delete_book
from .views import list_books, admin_view

from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
       
       # path('books/', views.list_books, name='book_list'),
        path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

        path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
        path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
        path('register/', views.register, name='register'),

        path('admin/dashboard/', admin_view, name='admin-dashboard'),
        path('librarian/dashboard/', librarian_view, name='librarian-dashboard'),
        path('member/dashboard/', member_view, name='member-dashboard'),

        path('book/add/', views.add_book, name='add_book'),
        path('book/edit/<int:book_id>/', views.edit_book, name='edit_book'),
        path('book/delete/<int:book_id>/',views.delete_book, name='delete_book'),
        path('books/', views.list_books, name='book_list'),
]

