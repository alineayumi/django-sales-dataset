from django import forms
from .models import Product, Sale

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ("product_name", "client_name", "quantity")

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name", "price")
