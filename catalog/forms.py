
from django import forms
from .models import Car, Seller, Buyer, Sale

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['model', 'year', 'price', 'mileage', 'description', 'image']

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['name', 'contact_info']

class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['name', 'contact_info']

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['car', 'seller', 'buyer', 'price']
