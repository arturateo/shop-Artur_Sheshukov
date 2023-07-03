from django import forms
from django.forms import widgets
from shop.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'select', 'price_coast', 'pic_img', 'balance']
        widgets = {'title': widgets.TextInput(attrs={'class': 'form-control'}),
                   'description': widgets.Textarea(attrs={'class': 'form-control'}),
                   'select': widgets.Select(attrs={'class': 'form-control'}),
                   'price_coast': widgets.NumberInput(attrs={'class': 'form-control'}),
                   'pic_img': widgets.TextInput(attrs={'class': 'form-control'}),
                   'balance': widgets.NumberInput(attrs={'class': 'form-control', 'min': 0})
                   }
