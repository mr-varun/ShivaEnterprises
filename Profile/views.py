from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user

from .forms import CreateUserForm, ProfileForm

# Create your views here.

@login_required(login_url='/ulogin/')
def home(request):
    return render(request, 'profiles/home.html')

@login_required(login_url='/ulogin/')
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance = request.user.profile)
        if form.is_valid():
            form.save()
            username = request.user.username
            messages.success(request, f'{username}, Your profile is updated.')
        pass
    else:
        form = ProfileForm(instance = request.user.profile)
    context = {'form':form}
    return render(request, 'profiles/profile.html', context)

@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f'{username}, you are logged in.')
            return redirect("/home/")
        else:
            messages.info(request, 'Invlid username or password.')
            return redirect('/ulogin/')
    return render(request, 'profiles/user_login.html')

@unauthenticated_user
def login_admin(request):
    return render(request, 'profiles/admin_login.html')

@unauthenticated_user
def register_user(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Account is created.')
            return redirect('/ulogin/')
        else:
            context = {'form': form}
            messages.info(request, 'Invalid credentials')
            return render(request, 'profiles/register_page.html', context)     
    context = {'form': form}
    return render(request, 'profiles/register_page.html', context)
    
@login_required(login_url='/ulogin/')
def logout_user(request):
    logout(request)
    messages.info(request, 'You logget out successfully')
    return redirect('/ulogin/')