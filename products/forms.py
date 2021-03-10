from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]


class RawProductForm(forms.Form):
    title = forms.CharField(label='Product Title')
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                            attrs={
                                                'cols': 120,
                                                'placeholder': 'Description'
                                            }),
                                  label='')
    price = forms.DecimalField(initial=99.99)

