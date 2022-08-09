from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
from .models import ToDo
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'todo/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {"form": UserCreationForm()})
    else:
        # Create a new user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')

            except IntegrityError:
                return render(request, 'todo/signupuser.html', {"form": UserCreationForm(), 'error': 'That username has already been taken. Please choose another one, bitch.'})
        else:
            # Tell about the error
            return render(request, 'todo/signupuser.html', {"form": UserCreationForm(), 'error': 'Password did not match, dumbass'})

@login_required()
def currenttodos(request):
    todos = ToDo.objects.filter(creator=request.user, datecomplited__isnull=True)
    return render(request, 'todo/currenttodos.html', {'todos': todos})

@login_required()
def complitedtodos(request):
    todos = ToDo.objects.filter(creator=request.user, datecomplited__isnull=False).order_by('-datecomplited')
    return render(request, 'todo/complitedtodos.html', {'todos': todos})

@login_required()
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {"form": AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todo/loginuser.html', {"form": AuthenticationForm(), 'error': 'User or password didnt match, jerk'})
        else:
            login(request, user)
            return redirect('currenttodos')

@login_required()
def createtodo(request):
    if request.method == 'GET':
        return render(request, 'todo/createtodo.html', {"form": TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.creator = request.user
            newtodo.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/createtodo.html', {"form": TodoForm(), 'error': 'Bad data passed in'})

@login_required()
def viewtodo(request, todo_pk):
    todo = get_object_or_404(ToDo, pk=todo_pk, creator=request.user)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'todo/detail.html', {'todo': todo, 'form': form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/detail.html', {'todo': todo, 'form': form, 'error':'bad info'})

@login_required()
def completetodo(request, todo_pk):
    todo = get_object_or_404(ToDo, pk=todo_pk, creator=request.user)
    if request.method == 'POST':
        todo.datecomplited = timezone.now()
        todo.save()
        return redirect('currenttodos')

@login_required()
def deletetodo(request, todo_pk):
    todo = get_object_or_404(ToDo, pk=todo_pk, creator=request.user)
    if request.method == 'POST':
        # todo.datecomplited = timezone.now()
        todo.delete()
        return redirect('currenttodos')