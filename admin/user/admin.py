from django.contrib import admin
from .models import User, ShelterHome, Details


admin.site.register(User)
admin.site.register(Details)
admin.site.register(ShelterHome)
