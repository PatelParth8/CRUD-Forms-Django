from django import forms
from .models import *

#Create Your forms Here
class BookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = '__all__'

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'

class LoginForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['email', 'password']