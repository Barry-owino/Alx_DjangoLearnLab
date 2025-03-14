from django.urls import path
from .views import (
    BookListCreateView,
    BookRetrieveUpdateDestroyView,
    AuthorListCreateView
)

urlpatterns = [
    # Book endpoints
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), 
         name='book-detail'),
    
    # Author endpoints
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
]
