from django import forms
from .models import *

class CustomerForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = ['name', 'phone', 'email', 'address']

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = invoice
        fields = ['customer', 'date', 'amount', 'status']
        widgets = {
            'date':forms.DateInput(
                attrs ={'placeholder':'YYY-MM-DD','type':'date'}
            ),
        }
