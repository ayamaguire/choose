from django.db import models
from .book import Book


class Question(models.Model):
    """ Questions model; takes at least one choice, points to the next question
    """
    text = models.CharField(max_length=200)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
