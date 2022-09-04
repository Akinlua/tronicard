
from django.shortcuts import render, redirect
from .form import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from .form import ProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
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
            try:
                Profile.objects.get(email = user.email)
            except:
                user.save()
                login(request, user)
                messages.success(request, 'User account was created!')
                return redirect('home')
            if Profile.objects.get(email = user.email):
                messages.error(request, 'Email have an account already')
        else:
            messages.error(request, 'An error occured')
           
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
        
        else:
            messages.error(request,'Username or Password is incorrect')

    context={'page':page}
    return render(request, 'users/create-login.html', context)

@login_required(login_url='login')
def account(request):
    user= request.user
    profile= request.user.profile
    context={'profile':profile, 'user':user}
    return render(request, 'users/account.html', context)

def editaccount(request):
    user= request.user
    user_profile= request.user.profile
    form = ProfileForm(instance=user_profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            profile=form.save(commit=False)
            # emails
            emails = Profile.objects.values_list('email', flat=True) 
            mass_emails=[] 
            for i in emails: 
                mass_emails.append(i)
            mass_emails.remove(user.email)
            # usernames
            username = Profile.objects.values_list('username', flat=True) 
            mass_usernames=[] 
            for i in username: 
                mass_usernames.append(i)
            mass_usernames.remove(user.username)
            print(user.username)
            print(mass_usernames)
            print(mass_emails)
            print(profile.username)
            # users= Profile.objects.exclude(username=user_profile.username)
            if (profile.username in mass_usernames) or (profile.email in mass_emails) :
                messages.error(request, 'Username or Email Taken')
            else:
                user.username= profile.username
                user.email= profile.email
                user.first_name= profile.name
                user.save()
                profile.save()
                return redirect('account')
        else:
            messages.error(request,'Username or Email already exist')
    context={'form':form}
    return render(request, 'users/edit account.html', context)