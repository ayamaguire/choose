from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Book, Question, Choice


def index(request):
    book_list = Book.objects.all()
    context = {
        'book_list': book_list,
    }
    return render(request, 'choose/index.html', context)


def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'choose/detail.html', {'book': book})


def question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'choose/question.html', {'question': question})


def follow(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'choose/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        next_question = selected_choice.directs_to
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('choose:question', args=(next_question.id,)))
