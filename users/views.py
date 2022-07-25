
from django.shortcuts import render, redirect
from .form import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def logoutUser(request):
    logout(request)
    return redirect('login')

def createAccount(request):
    form=CustomUserCreationForm()
    page='create'
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('account')
    context={'form':form, 'page':page}
    return render(request, 'users/create-login.html', context)

def loginUser(request):
    page= 'login'
    if request.method == 'POST':
        username= request.POST['Username']
        password= request.POST['Password']

        try:
            user= User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user= authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'home')

    context={'page':page}
    return render(request, 'users/create-login.html', context)

def account(request):
    return render(request, 'users/account.html')