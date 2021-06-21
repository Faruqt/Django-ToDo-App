from django.urls import path, include
from .views import categories

app_name = 'category'

urlpatterns = [
    path('', categories, name='my_categories'),
]