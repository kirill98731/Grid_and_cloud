from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Task
from django.http import JsonResponse
import subprocess

def log(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['user'], password=request.POST['pass'])
        if user and user.is_active == True:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'worker/log.html', {'message': 'Неверный логин или пароль'})

    return render(request, 'worker/log.html')


def sign(request):
    if request.method == 'POST':
        try:
            user = User.objects.create_user(username=request.POST['user'], password=request.POST['pass'])
            user.save()
        except:
            pass

        return redirect('/')

    return render(request, 'worker/sign.html')

def index(request):
    if '_auth_user_id' not in request.session.keys():
        return redirect('/login')

    user = User.objects.get(id=request.session['_auth_user_id'])
    tasks = Task.objects.filter(user=user)
    return render(request, 'worker/index.html', {'tasks': tasks})


def out(request):
    logout(request)
    return redirect('/')

def add(request) :
    task = Task(name=request.POST['name'], type=request.POST['type'], input_data=request.POST['input_data'], status=False, user=request.user)
    task.save()
    tasks_count = len(Task.objects.filter(status=False))
    if tasks_count >= 2:
        subprocess.Popen("bash script.sh", shell=True)
    return redirect('/')

