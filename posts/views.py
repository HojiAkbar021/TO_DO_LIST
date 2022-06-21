from turtle import title
from django.shortcuts import redirect, render
from .models import Task
from django.db.models import Q
from django.contrib import messages

# Create your views here.
def task_detail(request, id):
    task = Task.objects.get(id = id)
    return render(request, 'blog_detail.html')


def task_create(request):
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            description = request.POST.get('description')
            time = request.POST.get('time')
            task_obj = Task.objects.create(user = request.user, title = title, description = description, time = time)
            return redirect('profile', request.user.id)
        except:
            messages.error(request, 'Неправильные данные')
    return render(request, 'task_creat.html')


def task_update(request, id):
    task = Task.objects.get(id = id)
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            description = request.POST.get('description')
            time = request.POST.get('time')
            task = Task.objects.get(id = id)
            task.title = title 
            task.description = description 
            task.time = time
            task.save()
            return redirect('profile', request.user.id)
        except:
            messages.error(request, 'Неправильные данные')
            
    context = {
        'task' : task,
    }
    return render(request, 'task_update.html', context)


def task_delete(request, id):
    if request.method == 'POST':
        task = Task.objects.get(id = id)
        task.delete()
        return redirect('profile', request.user.id)
    return render(request, 'task_delete.html')


def task_search(request):
    tasks = Task.objects.all()
    qury_obj = request.GET.get('key')
    if qury_obj:
        tasks = Task.objects.filter(Q(title__icontains = qury_obj))
    if qury_obj == "":
        return redirect('profile', request.user.id)
    context = {
        'tasks' : tasks
    }
    return render(request, 'task_search.html', context)