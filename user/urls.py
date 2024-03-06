from django.urls import path
from .views import login_page, register_page, landingpage, encode_msg_into_img, report_crime, appointment_success, details

urlpatterns = [

    path('', landingpage, name='landingpage'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),

    path('details/', details, name='details'),
    path('appointment_success/', appointment_success, name='appointment_success'),

    path('encode/', encode_msg_into_img, name='encode_msg_into_img'),
    path('report/', report_crime, name='report_crime'),
]
