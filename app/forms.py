from django import forms
from .models import Contacto, Producto, Producto_Oferta
from django.contrib.auth.forms import UserCreationForm


class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    pass


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'  
    
class ProductoOfertaForm(forms.ModelForm):
    class Meta:
        model = Producto_Oferta
        fields = '__all__'