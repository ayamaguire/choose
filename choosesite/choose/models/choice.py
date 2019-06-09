from django.db import models
from .question import Question


class Choice(models.Model):
    """ Choice model; a path to take, an option. Belongs to a question
    """
    text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    directs_to = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='directs_to')

    def __str__(self):
        return self.text
