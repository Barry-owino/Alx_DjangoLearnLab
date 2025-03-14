from django.urls import path
from .views import (
    BookListCreateView,
    BookRetrieveUpdateDestroyView
)

urlpatterns = [
    # Combined list/create endpoint
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    
    # Combined detail/update/delete endpoint
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
]
