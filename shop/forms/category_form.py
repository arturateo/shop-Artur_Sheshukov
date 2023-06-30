from django import forms
from django.forms import widgets
from shop.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description']
        widgets = {'title': widgets.TextInput(attrs={'class': 'form-control'}),
                   'description': widgets.Textarea(attrs={'class': 'form-control'})}