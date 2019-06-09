from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:book_id>/questions/', views.questions, name='questions'),
    # ex: /polls/5/vote/
    path('<int:question_id>/follow/', views.follow, name='follow'),
]