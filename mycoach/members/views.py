from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from .models import Member
import csv


def login_user(request):
    """This logs in the user"""
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, 'Invalid username or password.')
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request) -> redirect:
    """This logs out the user"""
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')

def register_user(request):
    """This registers the user"""
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get['username']
            password = form.cleaned_data.get['password1']
            user = authenticate(username=username, password=password1)
            login(request, user)
            messages.success(request, 'Account created for ' + username)
            return redirect('home')
    else:
        form = RegisterUserForm()

    return render(request, 'authenticate/register_user.html', {
        'form': form,
    })

def athletes(request):
    """This renders the athletes page"""
    members = Member.objects.all()
    try:
        with open('members.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skips header row
            members = list(reader)
        return render(request, 'mains/athletes.html', 
        {
            'members': members,
        })
    except FileNotFoundError:
        messages.error(request, 'File not found')
        return redirect('home')

def add_athlete(request):
    """This renders the add athlete page"""
    submitted = False
    if request.method == 'POST':
        form = AthleteForm(request.POST, request.FILES)
        if form.is_valid():
            athlete = form.save(commit=False)
            athlete.name = request.user.id # User that's logged in
            athlete.save()
            return HttpResponseRedirect('/add_athlete?submitted=True')
    else:
        form = AthleteForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'mains/add_athlete.html', {
        'form': form,
        'submitted': submitted
    })

def view_athlete(request):
    """This shows the selected athlete on a separate page"""
    athlete = Member.objects.get(pk=id)
    return render(request, 'mains/view_athlete.html', {
        'athlete': athlete,
    })
