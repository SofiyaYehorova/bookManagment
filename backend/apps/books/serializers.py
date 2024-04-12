from rest_framework import serializers

from .models import BookModel


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel

        fields = ('id', 'name', 'author', 'published', 'ISBN',)
