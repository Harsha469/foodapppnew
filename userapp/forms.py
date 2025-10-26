from django import forms 
from . models import User 

class ProductForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','product_name','price','image']

        