from datetime import datetime, timezone

from django.shortcuts import render, redirect

from .models import User, Task, Record
from .forms import SignUpForm, TaskForm

# def calculate_task_points(task):
#     last_completed = task.last_completed
#     seconds = (datetime.now(timezone.EST) - last_completed).seconds
#     timley_reward = seconds / task.period

#     # TODO calculate average preference spectrum score
#     avg_ps_score = -50
#     return round(-avg_ps_score * timley_reward)

def records(request):
    if not request.user.is_authenticated:
        return redirect("/login/")

    todo_records = Record.objects.filter(time_completed=None)
    for record in todo_records:
        print(record)
    # points = [calculate_task_points(record.task) for record in todo_records]
    points = [0 for _ in range(len(todo_records))]
    todo_records = [record for _,record in sorted(zip(points, todo_records))]
    done_records = Record.objects.exclude(time_completed__isnull=True).order_by("time_completed")

    for i, record in enumerate(todo_records):
        record.points = points[i]

    context = {
        "todo": todo_records,
        "done": done_records
    }
    
    return render(request, "tasks/records.html", {})


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data
            user = User.objects.create_user(f["username"], None, f["password"])
            user.first_name = f["first_name"]
            user.last_name = f["last_name"]
            user.save()
            return redirect("/login/")
    else:
        form = SignUpForm()
    
    return render(request, "tasks/signup.html", {"form": form})

def tasks(request, delete_id=None):
    if not request.user.is_authenticated:
        return redirect("/login/")

    if delete_id is not None:
        task = Task.objects.filter(id=delete_id)
        if task.exists():
            task.delete()
        return redirect("/tasks/")

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            form = TaskForm()

            new_task.author = request.user
            new_task.last_completed = datetime.now()
            new_task.save()

            record = Record(task=new_task)
            record.save()
    else:
        form = TaskForm()
    
    context = {
        "tasks": Task.objects.order_by("period"),
        "form": form,
    }
    return render(request, "tasks/tasks.html", context)

def points(request):
    if not request.user.is_authenticated:
        return redirect("/login/")
    context = {
        "users": User.objects.filter(is_staff=0).order_by("points")
    }
    return render(request, "tasks/points.html", context)

def preference_spectrum(request):
    if not request.user.is_authenticated:
        return redirect("/login/")
    
    if request.method == "POST":
        pass
    else:
        pass

    return render(request, "tasks/preference_spectrum.html", {})
