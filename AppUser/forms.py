from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField()
    password1: forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2: forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}

class EditarUsuarioForm(UserCreationForm):
    email = forms.EmailField(label='Modificar email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password1 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}