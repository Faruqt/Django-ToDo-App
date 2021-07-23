from django.shortcuts import render,redirect
from .models import TodoList
from django.utils import timezone
from category.models import Category
from profiles.models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def my_todos(request): 
    user= request.user
    now = timezone.now().strftime("%Y-%m-%d")
    todos = TodoList.objects.filter(user=user) 
    category1 = Category.objects.get(id=1) 
    category2 = Category.objects.get(id=2) 
    category3 = Category.objects.get(id=3) 
    

    user_name=request.user.username  #get username
    Task_ID_Business = TodoList.objects.filter(category__name="Business", user=user) 
    Task_ID_Personal = TodoList.objects.filter(category__name="Personal", user=user)
    Task_ID_Other = TodoList.objects.filter(category__name="Other", user=user)

    no_of_Task_ID_Business=len(Task_ID_Business)
    no_of_Task_ID_Personal=len(Task_ID_Personal)
    no_of_Task_ID_Other=len(Task_ID_Other)

    context = {

        "DateNow" : now,
        "todos": todos, 
        "username": user_name,
        "category_i":category1,
        "category_ii":category2,
        "category_iii":category3,
        "no_of_business_tasks":no_of_Task_ID_Business,
        "no_of_other_tasks":no_of_Task_ID_Other,
        "no_of_personal_tasks":no_of_Task_ID_Personal,

    }

    return render(request, "todolist/home.html", context)


