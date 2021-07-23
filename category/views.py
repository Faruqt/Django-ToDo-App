from django.shortcuts import render
from django.utils import timezone
from .models import Category
from todolist.models import TodoList
from profiles.models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def categories(request): 
    user= request.user
    now = timezone.now().strftime("%Y-%m-%d")
    todos = TodoList.objects.filter(user=user) 
    categories = Category.objects.all() 
    check= None
  
    if request.method == "POST": 
        if "taskAdd" in request.POST: 
            title = request.POST["description"] 
            date = str(request.POST["date"]) 
            time = str(request.POST["time"])
            category = request.POST["category_select"]
            content = title + "  at " + time + " on " + date + " [" + category + " ]" 
            Todo = TodoList(title=title, content=content, time=time, due_date=date, category=Category.objects.get(name=category),user=user)
            Todo.save()  
           
            
        if "taskDelete" in request.POST: 
            if "checkedbox" in request.POST: 
                deleteTask = request.POST["checkedbox"]
                todo = TodoList.objects.get(id=int(deleteTask)) 
                todo.delete() 
            else:
                check = 'Please check-box of task to be deleted'

    context = {
        "DateNow" : now,
        "todos": todos, 
        "categories":categories,
        "check":check,
    }

    return render(request, "category/category.html", context)
