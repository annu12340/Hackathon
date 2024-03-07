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

class SteganographyForm(forms.Form):
    user_input = forms.CharField(label='Enter your input', max_length=100)

    
class CulpritDetailsForm(forms.ModelForm):
    class Meta:
        model = CulpritDetails
        fields = '__all__'