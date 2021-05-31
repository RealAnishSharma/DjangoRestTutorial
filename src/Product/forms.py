from django import forms
from django.db import models
from .models import Product

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name','description','price','image')