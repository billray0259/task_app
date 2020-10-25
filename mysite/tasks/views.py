from django.shortcuts import render, redirect

from .models import User, Task
from .forms import SignUpForm, TaskForm


def index(request):
    context = {
        "users": User.objects.order_by("points")
    }
    return render(request, "tasks/index.html", context)


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save() 
            form = SignUpForm()
    else:
        form = SignUpForm()
    
    return render(request, "tasks/signup.html", {"form": form})

def tasks(request, delete_id=None):
    if not request.user.is_authenticated:
        return redirect("login/")

    if delete_id is not None:
        task = Task.objects.filter(id=delete_id)
        if task.exists():
            task.delete()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            form = TaskForm()

            new_task.author = request.user
            new_task.save()
    else:
        form = TaskForm()
    
    context = {
        "tasks": Task.objects.order_by("period"),
        "form": form,
    }
    return render(request, "tasks/tasks.html", context)

def preference_spectrum(request):
    if request.method == "POST":
        pass
    else:
        pass

    return render(request, "tasks/preference_spectrum.html", {})
