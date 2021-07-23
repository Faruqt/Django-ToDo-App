from django.db import models
from django.utils import timezone
from category.models import Category
from django.contrib.auth.models import User

# Create your models here.

class TodoList(models.Model): 
    
    title = models.CharField(max_length=250) 
    content = models.TextField(blank=True, null=True) 
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) 
    time = models.TimeField(auto_now=False,null=True)
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) 
    category = models.ForeignKey(Category, default="general", on_delete=models.CASCADE) 
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        ordering = ["-created"] #ordering by the created field
   
    def __str__(self):
        return self.title 
