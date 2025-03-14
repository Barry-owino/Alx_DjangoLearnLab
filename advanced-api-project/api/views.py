from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework
from .models import Book, Author
from .serializers import BookSerializer
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status

class BookListCreateView(generics.ListCreateAPIView):
    """
    GET: List books with filtering, search, and ordering
    - Filter by: title, author ID, publication year ranges
    - Search in: title and author names
    - Order by: title or publication year (asc/desc)
    
    POST: Create new book (authenticated only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    # Filter configuration
    filterset_fields = {
        'title': ['exact', 'icontains'],
        'author': ['exact'],
        'publication_year': ['exact', 'gte', 'lte']
    }
    
    # Search configuration
    search_fields = ['title', 'author__name']
    
    # Ordering configuration
    ordering_fields = ['title', 'publication_year']
    ordering = ['-publication_year']

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        """Handle book creation with custom validation"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Custom publication year validation
        pub_year = serializer.validated_data.get('publication_year')
        if pub_year > datetime.now().year:
            return Response(
                {"error": "Publication year cannot be in the future"},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )
