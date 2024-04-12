from django.utils.decorators import method_decorator

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from .models import BookModel
from .serializers import BookSerializer


@method_decorator(name='get', decorator=swagger_auto_schema(security=[]))
@method_decorator(name='post', decorator=swagger_auto_schema(security=[]))
class BooksListCreateAPIView(ListCreateAPIView):
    """
        get:
            List all books
        post:
            Create a new book
    """
    serializer_class = BookSerializer
    queryset = BookModel.objects.all()


@method_decorator(name='get', decorator=swagger_auto_schema(security=[]))
@method_decorator(name='put', decorator=swagger_auto_schema(security=[]))
@method_decorator(name='patch', decorator=swagger_auto_schema(security=[]))
@method_decorator(name='delete', decorator=swagger_auto_schema(security=[]))
class BooksRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    get:
        retrieve book by id
    put:
        update book by id
    patch:
        partial update book by id
    delete:
        delete book by id
        Retrieve, update or delete a book instance
    """
    serializer_class = BookSerializer
    queryset = BookModel.objects.all()
