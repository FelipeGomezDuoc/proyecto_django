from django import forms
from django.forms import ModelForm
from .models import Pelicula

class PeliculaForm(ModelForm):
    
    class Meta:
        model = Pelicula
        fields = ['nombre', 'duracion', 'año', 'genero']
        


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())