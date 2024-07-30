from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout  # Import the logout function
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email,
                    first_name=first_name, last_name=last_name
                )
                user.save()
                messages.success(request, 'User created successfully')
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('register')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth_logout(request)
    return redirect('index')

def aboutus(request):
    return render(request, 'aboutus.html')

def order(request):
    return render(request, 'order.html')

def checkout(request):
    return render(request, 'checkout.html')

def homepage(request):
    return render(request, 'homepage.html')
