from django.urls import path
from .views import login_page, register_page, landingpage, dashboard, user_details

urlpatterns = [

    path('', landingpage, name='landingpage'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('details/', user_details, name='details'),
    path('dashboard/', dashboard, name='dashboard'),
]
