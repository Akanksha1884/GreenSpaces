from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def dashboard(request):
    return render(request, 'dashboard.html')

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken')
            return redirect('register')
        
        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)
        
        # Log the user in
        login(request, user)
        
        return redirect('dashboard')
    else:
        return render(request, 'registration_form.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # Log the user in
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'login_form.html')

def forgot_password(request):
    if request.method == 'POST':
        # Process forgot password form submission
        email = request.POST.get('email')
        # Send password reset instructions to the user's email
        messages.success(request, 'Password reset instructions sent to your email')
        return redirect('login')
    else:
        # Render forgot password form
        return render(request, 'forgot_password.html')
