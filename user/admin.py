from django.contrib import admin
from .models import User, Appointments, Details


admin.site.register(User)
admin.site.register(Details)
admin.site.register(Appointments)
