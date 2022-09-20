from django import forms
from django.forms import TextInput, Select, FileInput, IntegerField, DateInput, CheckboxInput

from .models import *

class HeroImageForm(forms.ModelForm):
    class Meta:
        model = HeroImage
        fields = ['text','buy_text', 'image']
        widgets = {
            'text': TextInput(attrs={'class': 'form-control'}),
            'buy_text': TextInput(attrs={'class': 'form-control'}),
            'image': FileInput(attrs={'class': 'col-form-label'})
        }

class FeaturedCollectionForm(forms.ModelForm):
    class Meta:
        model = FeaturedCollection
        fields = ['text','buy_text', 'image']
        widgets = {
            'text': TextInput(attrs={'class': 'form-control'}),
            'buy_text': TextInput(attrs={'class': 'form-control'}),
            'image': FileInput(attrs={'class': 'col-form-label'})
        }

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['title','description', 'specs', 'price', 'stock', 'category']
#         widgets = {
#             'title': TextInput(attrs={'class': 'form-control'}),
#             'description': TextInput(attrs={'class': 'form-control'}),
#             'has_specs': CheckboxInput(attrs={'class': 'form-control'}),
#             'has_variant': CheckboxInput(attrs={'class': 'form-control'}),
#             'price': TextInput(attrs={'class': 'form-control'}),
#             'stock': TextInput(attrs={'class': 'form-control'}),
#         }

# class ProductImageForm(forms.ModelForm):
#     class Meta:
#         model = ProductImage
#         fields = ['name','image', 'ranking', 'product']
#         widgets = {
#             'name': TextInput(attrs={'class': 'form-control'}),
#             'image': FileInput(attrs={'class': 'col-form-label'}),
#             'ranking': TextInput(attrs={'class': 'form-control'}),
#             'product': Select(attrs={'class': 'form-control'}),
#         }

class InterestCheckForm(forms.ModelForm):
    class Meta:
        model = InterestCheck
        fields = ['title','discord', 'image']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'discord': TextInput(attrs={'class': 'form-control'}),
            'image': FileInput(attrs={'class': 'col-form-label'}),
        }

