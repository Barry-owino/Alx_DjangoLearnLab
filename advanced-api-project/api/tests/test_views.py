from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .models import Book, Author

User = get_user_model()

class BookAPITests(APITestCase):
    def setUp(self):
        # Create test data
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.token = Token.objects.create(user=self.user)
        self.author = Author.objects.create(name='J.K. Rowling')
        
        # Create test books
        self.book1 = Book.objects.create(
            title='Harry Potter 1',
            publication_year=2001,
            author=self.author
        )
        self.book2 = Book.objects.create(
            title='Harry Potter 2',
            publication_year=2002,
            author=self.author
        )
        self.book3 = Book.objects.create(
            title='The Hobbit',
            publication_year=1937,
            author=Author.objects.create(name='J.R.R. Tolkien')
        )

        # API endpoints
        self.list_url = reverse('book-list-create')
        self.detail_url = lambda pk: reverse('book-detail', args=[pk])

    def authenticate(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    # CRUD Tests
    def test_list_books_unauthenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_create_book_authenticated(self):
        self.authenticate()
        data = {
            'title': 'New Book',
            'publication_year': 2023,
            'author': self.author.id
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)

    def test_create_book_unauthenticated(self):
        data = {'title': 'Unauthorized Book'}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_book_detail(self):
        url = self.detail_url(self.book1.id)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_update_book_authenticated(self):
        self.authenticate()
        url = self.detail_url(self.book1.id)
        data = {'title': 'Updated Title'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Title')

    def test_delete_book_authenticated(self):
        self.authenticate()
        url = self.detail_url(self.book1.id)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)

    # Filter/Search/Order Tests
    def test_filter_by_author(self):
        response = self.client.get(self.list_url, {'author': self.author.id})
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['author'], 'J.K. Rowling')

    def test_filter_by_publication_year(self):
        response = self.client.get(
            self.list_url,
            {'publication_year__gte': 2000}
        )
        self.assertEqual(len(response.data), 2)

    def test_search_functionality(self):
        response = self.client.get(self.list_url, {'search': 'Hobbit'})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'The Hobbit')

    def test_ordering(self):
        response = self.client.get(self.list_url, {'ordering': '-publication_year'})
        years = [item['publication_year'] for item in response.data]
        self.assertEqual(years, [2002, 2001, 1937])

    # Validation Tests
    def test_create_book_future_year(self):
        self.authenticate()
        data = {
            'title': 'Future Book',
            'publication_year': 2050,
            'author': self.author.id
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Publication year cannot be in the future', str(response.data))

    def test_invalid_data_format(self):
        self.authenticate()
        data = {'publication_year': 'invalid-year'}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
