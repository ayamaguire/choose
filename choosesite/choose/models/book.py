from django.db import models


class Book(models.Model):
    """ Book model; essentially a directed graph of questions and choices
    """
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
