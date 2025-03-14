# api/views.py
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status

class BookListView(generics.ListAPIView):
    """
    GET: List all books (public access)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookDetailView(generics.RetrieveAPIView):
    """
    GET: Retrieve single book by ID (public access)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'pk'

class BookCreateView(generics.CreateAPIView):
    """
    POST: Create new book (authenticated users only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Custom validation example
        publication_year = serializer.validated_data.get('publication_year')
        if publication_year > datetime.now().year:
            return Response(
                {"error": "Future publication dates not allowed"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH: Update existing book (authenticated users only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE: Remove book (authenticated users only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'
