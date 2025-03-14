from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    #serializes Book model dta with validation includes - all model fields -custom validation for publication_year
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publications_year(self, value):
        #ensure publication year is not in the future
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(f"Publication year cannot be in the future (max {current_year})")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    #serializes Author model data with nested book relationships includes -name field -nested BookSerializer for related book
    books = BookSerializer(many=True, read_only=True, source='book')

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']



