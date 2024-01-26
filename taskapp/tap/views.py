from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Task

def index(request):
    tasks = Task.objects.filter(user=request.user)
    context = {
        'tasks':tasks
    }
    return render(request, 'todoapp/index.html', context)

def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        validate_user = authenticate(username=username, password=password)
        
        if validate_user is not None:
            
            login(request, validate_user)
            return redirect('home')
        else: 
            messages.error(request, 'Conta não encontrada, tente novamente com outras informações')
            return redirect('loginpage')
    return render(request, 'todoapp/login.html', {})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')    
        password = request.POST.get('password')
        
        if len(password) < 6:
            messages.error(request, 'Senha muito curta!')
            return redirect('registerpage')
        
        get_all_users = User.objects.filter(username=username)
        
        if get_all_users:
            messages.error(request, 'Usuario já existe!')
            return redirect('registerpage')
        
        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()
        
        messages.success(request, 'Usuário criado com sucesso!')
        return redirect('loginpage')
        
        
    
    return render(request, 'todoapp/register.html', {})


def register_new_task(request):
    if request.method == 'POST':
        new_task_name = request.POST.get('taskname')
        new_task_description = request.POST.get('taskdescription')
        new_task = Task(user=request.user, task_name=new_task_name, 
                        task_description=new_task_description)
        new_task.save()
        return redirect('home')
        
        
    return render(request, 'todoapp/newtask.html', {})