from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'first_name', 'last_name', 'email', 'telephone',
            'address', 'postal_code', 'city', 'province', 'note',
            'transport'
        ]

        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control','id':'1'}
            ),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control','id':'2'}
            ),
            'email': forms.TextInput(
                attrs={'class': 'form-control','id':'3'}
            ),
            'telephone': forms.TextInput(
                attrs={'class': 'form-control','id':'4'}
            ),
            'address': forms.TextInput(
                attrs={'class': 'form-control','id':'5'}
            ),
            'postal_code': forms.TextInput(
                attrs={'class': 'form-control','id':'6'}
            ),
            'city': forms.TextInput(
                attrs={'class': 'form-control','id':'7'}
            ),
            'province': forms.TextInput(
                attrs={'class': 'form-control px-2' ,'id':'8'}
            ),
            'note': forms.Textarea(
                attrs={'class': 'form-control','id':'9', 'rows': 1}
            ),

            'transport': forms.RadioSelect
        }
