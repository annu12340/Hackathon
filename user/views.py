from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm, CulpritDetailsForm
from .models import User, ShelterHome, Details, CulpritDetails
import folium, os, geocoder
import numpy as np
from sklearn.neighbors import BallTree,NearestNeighbors
import spacy
from steganography.encode import encode

# Load the spaCy model
nlp = spacy.load("en_core_web_md")

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



def get_embedding(desc):
    # Tokenize the description and average the word vectors to get the embedding
    tokens = nlp(desc)
    embedding = sum(token.vector for token in tokens) / len(tokens)
    return embedding

def find_similarity(new_desc):
    all_descriptions= CulpritDetails.objects.filter()
    embeddings = [get_embedding(desc) for desc in all_descriptions]

    # Initialize NearestNeighbors
    nn = NearestNeighbors(n_neighbors=2, algorithm='brute', metric='cosine')  # Using cosine distance for similarity

    # Fit the data
    nn.fit(embeddings)

    new_text = new_desc
    new_embedding = get_embedding(new_text).reshape(1, -1)  # Reshape for compatibility with NearestNeighbors

    # Find similar neighbors
    distances, indices = nn.kneighbors(new_embedding)
    
    print("Similar neighbors for '{}' are:".format(new_text))
    for neighbor_index in indices[0]:
        print(all_descriptions[neighbor_index])
    return indices

def report_crime(request):
    if request.method == 'POST':
        age = request.POST.get('age')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        eyes = request.POST.get('eyes')
        skin = request.POST.get('skin')
        facial_features = request.POST.get('facial_features')
        physical_features = request.POST.get('physical_features')
        other_details = request.POST.get('other_details')
        
        details = ''
        if age:
            details += f'A person of age {age}. '
        if height:
            details += f'A person of height {height}. '
        if weight:
            details += f'A person of weight {weight}. '
        if eyes:
            details += f'A person with {eyes} eyes. '
        if skin:
            details += f'A person with {skin} skin. '
        if facial_features:
            details += f'A person with facial features: {facial_features}. '
        if physical_features:
            details += f'A person with physical features: {physical_features}. '
        if other_details:
            details += f'Additional details: {other_details}.'

        # Create CulpritDetails object and save to the database
        culprit_details = CulpritDetails.objects.create(
            details=details
        )
        # find_similar_matchs=find_similarity(details)
        find_similar_matchs = [
        "John Doe - Age 35, Height 180cm, Weight 75kg",
        "Jane Smith - Age 28, Height 165cm, Weight 60kg",
        "Alex Johnson - Age 42, Height 175cm, Weight 80kg"
    ]
        context = {'descriptions': find_similar_matchs}
        return render(request, 'similar_culprit.html', context)
    else:
        form = CulpritDetailsForm()
    return render(request, 'report_crime.html', {'form': form})

def get_current_gps_coordinates():
    g = geocoder.ip('me')
    if g.latlng is not None:
        return g.latlng
    else:
        return None

def map(request):
    marker = folium.Map(location=[latitude, longitude], zoom_start=8)
    queryset = ShelterHome.objects.filter(remaining_capacity__gt=0)  
    database_coordinates = np.array([[obj.latitude, obj.longitude] for obj in queryset])
    
    # Convert degrees to radians for accurate distance calculation
    database_coordinates_rad = np.deg2rad(database_coordinates)
    
    latitude, longitude = get_current_gps_coordinates()
    query_point = np.array([[latitude, longitude]])  
    query_point_rad = np.deg2rad(query_point)
    
    # Construct BallTree
    tree = BallTree(database_coordinates_rad, metric='haversine')
    distances, indices = tree.query(query_point_rad, k=3)
    print(distances, indices)
    
    nearest_neighbors = [queryset[i] for i in indices[0]]
    for shelter_home in shelter_homes:
        popup_content = f'<strong>{shelter_home.name}</strong><br>'
        popup_content += f'Max Capacity: {shelter_home.max_capacity}<br>'
        popup_content += f'Current Capacity: {shelter_home.current_capacity}<br>'
        popup_content += f'Remaining Capacity: {shelter_home.remaining_capacity}<br>'
        
        folium.Marker([shelter_home.latitude, shelter_home.longitude],
                      popup=f'<strong>Shelter Home</strong><br>Max Capacity: {shelter_home.max_capacity}<br>Current Capacity: {shelter_home.current_capacity}',
                      tooltip=popup_content).add_to(marker)
    
    # Save the map as an HTML file
    marker.save(os.path.join(os.getcwd(), 'templates', 'map.html'))
    
    return render(request, 'map.html')