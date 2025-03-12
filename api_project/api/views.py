#from django.shortcuts import render
#from rest_framework import generics
from rest_framework import viewsets, permissions
from .models import Book
from .serializers import BookSerializer

# viewset
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminUser] #only admins can modify
