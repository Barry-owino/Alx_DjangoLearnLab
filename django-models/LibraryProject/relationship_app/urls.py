from django.urls import path
from .views import list_books, LibraryDetailView
#from .views import login_view, RegisterView, CustomLogoutView
from .views import admin_view, librarian_view, member_view
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
       
        path('books/', list_books, name='list_books'),
        path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

        path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
        path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
        path('register/', views.register, name='register'),

        path('admin/dashboard/', admin_view, name='admin-dashboard'),
        path('librarian/dashboard/', librarian_view, name='librarian-dashboard'),
        path('member/dashboard/', member_view, name='member-dashboard'),

]
