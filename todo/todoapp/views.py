from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import todo
# Create your views here.

def home(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        new_todo = todo(user = request.user, todo_name = task)
        new_todo.save()
    return render(request,'todoapp/todoo.html', {})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if len(password) < 3:
            messages.error(request, 'Password must be at least 3 characters')
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Error, username already exists.')
            return redirect('register')

            
        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()


        messages.success(request,'successfully created')
        return redirect('login')
    return render(request,'todoapp/register.html', {})

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        validate_user = authenticate(username=username, password=password)
        if validate_user is not None:
            login(request, validate_user)
            return redirect('home_page')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
        


    return render(request,'todoapp/login.html', {})


def logoutpage(request):
    return redirect('home_page')