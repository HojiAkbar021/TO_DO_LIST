from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.contrib.auth import login, authenticate
from posts.models import Task


def profile(request, id):
    user = User.objects.get(id = id)
    tasks = Task.objects.all()
    context = {
        'tasks' : tasks,
        'user' : user
        }

    return render(request, 'profile.html', context)


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        date_of_birth = request.POST.get('date_of_birth')
        tel = request.POST.get('tel')
        profile_image = request.FILES.get('profile_image')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            try:
                user = User.objects.create(username=username, first_name = first_name, last_name = last_name, date_of_birth = date_of_birth, tel = tel, profile_image = profile_image)
                user.set_password(password1)
                user.save()
                return redirect('login')
            except:
                messages.error(request, 'Неправильные данные')
        else:
            messages.error(request, 'Пароли отличаются')

    return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.get(username=username)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile', user.id)
        except:
            messages.error(request, "Неправильный логин или пароль")

    return render(request, 'login.html')


def profile_update(request, id):
    user = User.objects.get(id = id)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        tel = request.POST.get('tel')
        profile_image = request.FILES.get('profile_image')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            user = User.objects.get(id = id)
            user.first_name = first_name 
            user.last_name = last_name 
            user.date_of_birth = date_of_birth
            user.tel = tel
            user.profile_image = profile_image
            user.username = username
            user.set_password(password1)
            user.save()
            return redirect('profile', user.id)
        else:
            messages.error(request, 'Пароли отличаются')
    context = {
        'user' : user,
    }
    return render(request, 'profile_update.html', context)
    

def delete_profile(request, id):
    user = User.objects.get(id = id)
    if request.method == "POST":
        user = User.objects.get(id = id)
        user.delete()
        return redirect('login')
    context = {
        'user' : user
    }
    return render(request, 'profile_delete.html', context)