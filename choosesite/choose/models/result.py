from django.db import models
from .book import Book


class Result(models.Model):
    """ Just an event, but since it's the end, it's not associated with a question.
    """
    text = models.CharField(max_length=200)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
