import email
from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    #Go theo dang ma hoa pas
    password = forms.CharField(widget = forms.PasswordInput)
    email = forms.EmailField(label='Email')
