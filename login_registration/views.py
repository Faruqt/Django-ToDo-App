from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, LoginForm
# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('main')

def login_view(request):
    error_message = None
    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('todolist:my_todos')
    else:
        form = LoginForm()

    context = {
        'form': form,
        'error_message': error_message
    }

    return render(request, 'auth/login.html', context)

def registerUserView(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            
            if user is not None:
                login(request, user)
                return redirect('todolist:my_todos')
    
    else:
        form = CustomUserCreationForm()

    context= {'form':form}
    return render(request,'auth/register.html', context)

    
