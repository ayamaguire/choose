from django.contrib import admin
from .models import Book, Question, Event, Choice

admin.site.register(Book)
admin.site.register(Question)
admin.site.register(Event)
admin.site.register(Choice)
