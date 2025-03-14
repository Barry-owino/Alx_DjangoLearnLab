#from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# Create your views here.
class BookListCreateView(generics.ListCreateAPIView):
    # Handles: GET:List all books-public access, POST:create new book-authenticated users only

    queryset = Book.objects.all()
    serializers_class = BookSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.Allowany()]
        return [permissions.IsAuthenticated()]

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    #-GET:Retrieve single book, PUT/PATCH:Update book-authenticated, DELETE:Remove book-authenticared

    queryset = Book.objects.all()
    serializer_classs = BookSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.Allowany()]
        return [permissions.IsAuthenticated()]

class AuthorListCreateView(generics.ListCreateAPIView):
    #similar config for Author model
    querset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]
