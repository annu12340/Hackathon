from django import forms
from .models import User, UserDetails


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        }


class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['userid','name', 'blood_group']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
            'blood_group': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'blood_group'})
        }

