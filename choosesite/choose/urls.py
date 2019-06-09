from django.urls import path

from . import views

app_name = 'choose'
urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:book_id>/', views.detail, name='detail'),
    path('question/<int:question_id>/', views.question, name='question'),
    path('question/<int:question_id>/follow/', views.follow, name='follow'),
]