from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm, CulpritDetailsForm
from .models import User, ShelterHome, Details
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
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        Details.objects.create(name=name, email=email, age=age)
        return redirect('appointment_success')  
    return render(request, 'details.html')

def appointment_success(request):
    return render(request, 'appointment_success.html')


def encode_msg_into_img(request):
    if request.method == 'POST':
        hidden_text = request.POST.get('hidden_text')
        import_from_db = request.POST.get('import_from_db')
        if import_from_db == "yes":
            user_details=Details.objects.filter(name="sad")[0]
            hidden_text += f"\n\n My name is {user_details.name}. I am staying at {user_details.name}"
        encode("output", hidden_text)
        return render(request, 'result.html', {'hidden_text': hidden_text, 'import_from_db': import_from_db})
    else:
        return render(request, 'encode_msg_into_img.html')



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