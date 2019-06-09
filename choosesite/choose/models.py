from django.db import models


class Book(models.Model):
    """ Book model; essentially a directed graph of questions and choices
    """


class Question(models.Model):
    """ Questions model; takes at least one choice, points to the next question
    """


class Event(models.Model):
    """ Events model; something that happens in between questions
    """


class Choice(models.Model):
    """ Choice model; a path to take, an option. Belongs to a question
    """