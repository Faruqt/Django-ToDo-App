from django.urls import path
from .views import my_todos

app_name = 'todolist'

urlpatterns = [
    path('', my_todos, name='my_todos'),
]