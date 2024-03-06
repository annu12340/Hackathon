from django.urls import path
from .views import login_page, register_page, landingpage,appointment_success, dashboard, details

urlpatterns = [

    path('', landingpage, name='landingpage'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('dashboard/', dashboard, name='dashboard'),

    path('details/', details, name='details'),
    path('appointment_success/', appointment_success, name='appointment_success'),
]
