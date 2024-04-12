from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.books.models import BookModel


class BookApiTestCase(APITestCase):
    def test_create_book(self):
        new_book = {
            "name": "1984",
            "author": "George Orwell",
            "ISBN": "0-452-28423-6"
        }
        response = self.client.post(reverse('books_list_create'), new_book, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BookModel.objects.count(), 1)

    def test_retrieve_books(self):
        new_book = {
            "name": "1984",
            "author": "George Orwell",
            "ISBN": "0-452-28423-6"
        }
        response = self.client.get(reverse('books_list_create'), new_book, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(BookModel.objects.count(), 0)

    def test_update_retrieve_destroy_books_by_id(self):
        new_book = {
            "name": "1984",
            "author": "George Orwell",
            "published": "1984-12-31",
            "ISBN": "0-452-28423-6"
        }
        response_book = self.client.post(reverse('books_list_create'), new_book)
        print(response_book.status_code)
        print(response_book)
        pk = response_book.data['id']
        print(pk)

        new_book_put = {
            "name": "1984",
            "author": "George Oorwell",
            "published": "1986-12-31",
            "ISBN": "0-452-28423-6"
        }
        new_book_patch = {
            "ISBN": "0-48852-28423-6"
        }
        response_put = self.client.put(reverse('books_update_retrieve_destroy', args=(pk,)), new_book_put)
        response_patch = self.client.patch(reverse('books_update_retrieve_destroy', args=(pk,)), new_book_patch)
        response_destroy = self.client.delete(reverse('books_update_retrieve_destroy', args=(pk,)))
        #
        self.assertEquals(response_book.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response_put.data, new_book_put)
        self.assertEquals(response_patch.data, new_book_patch)
        self.assertEquals(response_destroy.status_code, status.HTTP_204_NO_CONTENT)
