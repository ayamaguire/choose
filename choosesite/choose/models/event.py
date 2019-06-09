from django.db import models
from .question import Question


class Event(models.Model):
    """ Events model; something that happens in between questions
    """
    text = models.CharField(max_length=1000)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
