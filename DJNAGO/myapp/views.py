from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_protect
import requests
import json

User = get_user_model()

def home(request):
    return render(request, 'home.html')

def index2(request):
    return render(request, 'index2.html')

def features2(request):
    return render(request, 'features2.html')

def business2(request):
    return render(request, 'business2.html')

def tasks(request):
    return render(request, 'tasks.html')

def calendar(request):
    return render(request, 'calendar.html')

def projects(request):
    return render(request, 'projects.html')

def about_us2(request):
    try:
        response = requests.get('http://localhost:5000/team')
        response.raise_for_status()
        team_data = response.json()
    except requests.exceptions.RequestException as e:
        team_data = {"error": "Could not retrieve data from Flask API.", "details": str(e)}
    return render(request, 'about_us2.html', {'team_data': team_data})

def inbox(request):
    return render(request, 'inbox.html')

def upcoming(request):
    return render(request, 'upcoming.html')

def my_work(request):
    return render(request, 'my_work.html')

def education(request):
    return render(request, 'education.html')

def home2(request):
    return render(request, 'home2.html')

def business(request):
    return render(request, 'business.html')

def features(request):
    return render(request, 'features.html')

def about_us(request):
    return render(request, 'about_us.html')

def signup(request):
    return render(request, 'signup.html')

@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(email=email).exists():
            messages.error(request, "User already exists")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "User registered successfully")
        return redirect('signup')

    return redirect('signup')

@csrf_protect
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            request.session.set_expiry(600)
            messages.success(request, "User Logged In Successfully")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid email or password")
            return redirect('dashboard')

    return redirect('dashboard')

# @login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    messages.success(request, "User Logged out Successfully")
    return redirect('home')

# API Interaction Functions

def get_tasks(request):
    try:
        response = requests.get('http://localhost:5000/tasks')
        response.raise_for_status()
        tasks = response.json()
        return render(request, 'tasks.html', {'tasks': tasks})
    except requests.exceptions.RequestException as e:
        return render(request, 'tasks.html', {'error': str(e)})

def add_task(request):
    if request.method == "POST":
        task_text = request.POST.get("task_text")
        priority = request.POST.get("priority")

        try:
            response = requests.post('http://localhost:5000/tasks', json={'text': task_text, 'priority': priority})
            response.raise_for_status()
            messages.success(request, "Task added successfully")
        except requests.exceptions.RequestException as e:
            messages.error(request, f"Error adding task: {str(e)}")

        return redirect('tasks')

def update_task(request, task_id):
    if request.method == "POST":
        task_text = request.POST.get("task_text")
        priority = request.POST.get("priority")

        try:
            response = requests.put(f'http://localhost:5000/tasks/{task_id}', json={'text': task_text, 'priority': priority})
            response.raise_for_status()
            messages.success(request, "Task updated successfully")
        except requests.exceptions.RequestException as e:
            messages.error(request, f"Error updating task: {str(e)}")

        return redirect('tasks')

def delete_task(request, task_id):
    try:
        response = requests.delete(f'http://localhost:5000/tasks/{task_id}')
        response.raise_for_status()
        messages.success(request, "Task deleted successfully")
    except requests.exceptions.RequestException as e:
        messages.error(request, f"Error deleting task: {str(e)}")

    return redirect('tasks')
