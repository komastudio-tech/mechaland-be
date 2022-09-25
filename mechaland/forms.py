from django import forms
from django.forms import TextInput, Select, FileInput, IntegerField, DateInput

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

class UpdatesForm(forms.ModelForm):
    class Meta:
        model = Updates
        fields = ['title','text', 'category']
        kategori = (('Keyboard Kit', 'Keyboard Kit'),('PBTFans', 'PBTFans'))
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'text': TextInput(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': "form-control"}, choices=kategori)
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','description', 'has_specs', 'has_variant', 'price', 'stock', 'category']
        kategori = (('In Stock', 'In Stock'),('Live', 'Live'),('Preorder', 'Preorder'),('Groupbuy', 'Groupbuy'))
        true_false = ((True, 'Yes'), (False, 'No'))
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': TextInput(attrs={'class': 'form-control'}),
            'price': TextInput(attrs={'class': 'form-control'}),
            'stock': TextInput(attrs={'class': 'form-control'}),
            'has_specs' : Select(attrs={'class': "form-control"}, choices=true_false),
            'has_variant' : Select(attrs={'class': "form-control"}, choices=true_false),
            'category': Select(attrs={'class': "form-control"}, choices=kategori)
        }

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['name','image', 'ranking', 'product']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'image': FileInput(attrs={'class': 'col-form-label'}),
            'ranking': TextInput(attrs={'class': 'form-control'}),
            'product': Select(attrs={'class': 'form-control'}),
        }

class ProductSpecsForm(forms.ModelForm):
    class Meta:
        model = ProductSpecs
        fields = ['specs','product']
        widgets = {
            'specs': TextInput(attrs={'class': 'form-control'}),
            'product': Select(attrs={'class': 'form-control'}),
        }

class ProductVariantForm(forms.ModelForm):
    class Meta:
        model = ProductVariant
        fields = ['variant','price','stock','product']
        widgets = {
            'variant': TextInput(attrs={'class': 'form-control'}),
            'price': TextInput(attrs={'class': 'form-control'}),
            'stock': TextInput(attrs={'class': 'form-control'}),
            'product': Select(attrs={'class': 'form-control'}),
        }


class InterestCheckForm(forms.ModelForm):
    class Meta:
        model = InterestCheck
        fields = ['title','text', 'discord', 'image']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'text': TextInput(attrs={'class': 'form-control'}),
            'discord': TextInput(attrs={'class': 'form-control'}),
            'image': FileInput(attrs={'class': 'col-form-label'}),
        }

