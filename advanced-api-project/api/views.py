from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status

class BookListCreateView(generics.ListCreateAPIView):
    """
    GET: List all books (public)
    POST: Create new book (authenticated)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve book (public)
    PUT: Full update (authenticated)
    PATCH: Partial update (authenticated)
    DELETE: Remove book (authenticated)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
