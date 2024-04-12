from django.urls import path

from .views import BooksRetrieveUpdateDestroyAPIView, BooksListCreateAPIView

urlpatterns = [
    path('', BooksListCreateAPIView.as_view(), name='books_list_create'),
    path('/<int:pk>', BooksRetrieveUpdateDestroyAPIView.as_view(), name='books_update_retrieve_destroy'),
]
