from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Book


def index(request):
    book_list = Book.objects.all()
    template = loader.get_template('choose/index.html')
    context = {
        'book_list': book_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, book_id):
    return HttpResponse("You're looking at book %s." % book_id)


def questions(request, book_id):
    response = "You're looking at the questions of question %s."
    return HttpResponse(response % book_id)


def follow(request, question_id):
    return HttpResponse("You're following a choice on question %s." % question_id)
