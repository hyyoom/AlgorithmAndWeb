from django.shortcuts import render,redirect
from .forms import TodoFrom
from .models import Todo
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos' : todos
    }
    return render(request,'todos/index.html',context)


@login_required
def create(request):
    if request.method=="POST":
        form = TodoFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos:index')
    else:
        form = TodoFrom()
    context = {
        'form' : form
    }
    return render(request,'todos/create.html', context)


@login_required
def delete(request,pk):
    if request.method=="POST":
        form = Todo.objects.get(pk=pk)
        form.delete()
    return redirect('todos:index')



def todo_complete(request,pk):
    if request.method=="POST":
        todo = Todo.objects.get(pk=pk)
        if todo.complete == False:
            todo.complete = True
        else:
            todo.complete = False
        todo.save()
    return redirect('todos:index')