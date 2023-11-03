from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.

from django.shortcuts import render, redirect
from .forms import SignUpForm, LogInForm, AppForm, AppTaskForm
from .models import User, App, AppTask

# Sign Up page

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'user'
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# Login Page

def login_view(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username, password=password)
                # Creating a cookie
                if user.role == 'admin':
                    response = redirect('adminDashboard')
                else:
                    response = redirect('dashboard')
                response.set_cookie('user_name', user.username)
                return response
            except:
                return HttpResponse('Invalid username or password')
    else:
        form = LogInForm()

    return render(request, 'login.html', {'form': form})

def dashboard(request):
    user_data = User.objects.get(username=request.COOKIES.get('user_name'))
    apps = App.objects.all()
    print("hello")
    return render(request, 'dashboard.html', {'user_data': user_data,'apps': apps})

def adminDashboard(request):
    user_data = User.objects.get(username=request.COOKIES.get('user_name'))
    apps = App.objects.all()
    return render(request, 'adminDashboard.html', {'user_data': user_data,'apps': apps})

def logout_view(request):
    response = redirect('login')
    response.delete_cookie('user_name')
    return response

def app_create(request):
    if request.method == 'POST':
        form = AppForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app_create')
    else:
        form = AppForm()
    user_data = User.objects.get(username=request.COOKIES.get('user_name'))
    return render(request, 'app_create.html', {'user_data': user_data,'form': form})

def upload_screenshot(request, app_id):
    app = App.objects.get(id=app_id)
    user_data = User.objects.get(username=request.COOKIES.get('user_name'))
    if request.method == 'POST':
        form = AppTaskForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.uid = user_data
            data.aid = app
            form.save()
            return redirect('dashboard')
    else:
        form = AppTaskForm()
    return render(request, 'uploadScreenshot.html', {'user_data': user_data,'app':app,'form': form})

def profile(request):
    user_data = User.objects.get(username=request.COOKIES.get('user_name'))
    return render(request, 'profile.html', {'user_data': user_data})

def points(request):
    user_data = User.objects.get(username=request.COOKIES.get('user_name'))
    app_tasks = AppTask.objects.filter(uid = user_data)
    total_points = 0
    for app_task in app_tasks:
        total_points +=app_task.aid.points
    print(total_points)
    return render(request, 'points.html', {'user_data': user_data, 'app_tasks':app_tasks,'total_points':total_points})

def tasks(request):
    user_data = User.objects.get(username=request.COOKIES.get('user_name'))
    app_tasks = AppTask.objects.filter(uid = user_data)
    return render(request, 'tasks.html', {'user_data': user_data,'app_tasks':app_tasks})