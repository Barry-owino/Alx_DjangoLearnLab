from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    """
    GET: List books with filtering, search, and ordering
    Available query parameters:
    - ?author=1 → Filter by author ID
    - ?publication_year=2023 → Filter by publication year
    - ?search=potter → Search title and author fields
    - ?ordering=title → Order by title (asc)
    - ?ordering=-publication_year → Order by year (desc)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    # Filter configuration
    filterset_fields = {
        'author': ['exact'],
        'publication_year': ['exact', 'gte', 'lte']
    }
    
    # Search configuration
    search_fields = ['title', 'author__name']
    
    # Ordering configuration
    ordering_fields = ['title', 'publication_year']
    ordering = ['-publication_year']  # Default ordering

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
