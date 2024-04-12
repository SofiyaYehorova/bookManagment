from django.core import validators as V
from django.db import models

from core.enums.regex_enum import Regex


class BookModel(models.Model):
    class Meta:
        db_table = 'books'
        ordering = ['id']

    name = models.CharField(max_length=100, validators=[V.RegexValidator(Regex.NAME.pattern, Regex.NAME.msg)])
    author = models.CharField(max_length=100, validators=[V.RegexValidator(Regex.AUTHOR.pattern, Regex.AUTHOR.msg)])
    published = models.DateTimeField(auto_now_add=True)
    ISBN = models.CharField(max_length=20, validators=[V.RegexValidator(Regex.ISBN.pattern, Regex.ISBN.msg)])
