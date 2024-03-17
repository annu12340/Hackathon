from django import forms
from .models import User, Details, CulpritDetails


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        }


class DetailsForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = ['name', 'age', 'email']

class CulpritDetailsForm(forms.ModelForm):
    class Meta:
        model = CulpritDetails
        fields = '__all__'