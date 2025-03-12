from django.ulrs import path
from .views import BookList

urlpatterns = [
        path('books/', BookList.as_view(), name='book-list'),
]
