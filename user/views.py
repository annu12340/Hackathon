from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm, DetailsForm, SteganographyForm, CulpritDetailsForm
from .models import User, ShelterHome
import folium, os

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


def map(request):
    shelter_homes = ShelterHome.objects.filter(remaining_capacity__gt=0)  # Filter ShelterHome objects with num_people > 0
   
    m = folium.Map(location=[22.3601, 21.0589], zoom_start=12)
    
    for shelter_home in shelter_homes:
        popup_content = f'<strong>{shelter_home.name}</strong><br>'
        popup_content += f'Max Capacity: {shelter_home.max_capacity}<br>'
        popup_content += f'Current Capacity: {shelter_home.current_capacity}<br>'
        popup_content += f'Remaining Capacity: {shelter_home.remaining_capacity}<br>'
        
        folium.Marker([shelter_home.latitude, shelter_home.longitude],
                      popup=f'<strong>Shelter Home</strong><br>Max Capacity: {shelter_home.max_capacity}<br>Current Capacity: {shelter_home.current_capacity}',
                      tooltip=popup_content).add_to(m)
    
    # Save the map as an HTML file
    m.save(os.path.join(os.getcwd(), 'templates', 'map.html'))
    
    return render(request, 'map.html')