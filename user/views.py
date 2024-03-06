from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm, DetailsForm, SteganographyForm, CulpritDetailsForm
from .models import User
# from xyz.models import Abc

from steganography.encode import encode

def user_exist(credential):
    username = credential.cleaned_data.get("username")
    password = credential.cleaned_data.get("password")
    user = User.objects.filter(username=username, password=password)
    if user:
        return True
    else:
        return False


def valid_username(credential):
    username = credential.cleaned_data.get("username")
    user = User.objects.filter(username=username)
    if user:
        return False
    else:
        return True


def login_page(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            if user_exist(form):
                messages.add_message(request, messages.INFO, 'Logged in!')
                return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'user/login.html', context)


def register_page(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid() and valid_username(form):
            form.save()
            return redirect('/user/login')
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)


def landingpage(request):
    return render(request, 'home.html')


def details(request):
    if request.method == 'POST':
        form = DetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_success')
    else:
        form = DetailsForm()
    return render(request, 'details.html', {'form': form})

def appointment_success(request):
    return render(request, 'appointment_success.html')


def encode_msg_into_img(request):
    if request.method == 'POST':
        form = SteganographyForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['user_input']
            encode("output", message)
            return render(request, 'result.html', {'user_input': message})
    else:
        form = SteganographyForm()
    return render(request, 'encode_msg_into_img.html', {'form': form})


def report_crime(request):
    if request.method == 'POST':
        form = CulpritDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_success')
    else:
        form = CulpritDetailsForm()
    return render(request, 'report_crime.html', {'form': form})