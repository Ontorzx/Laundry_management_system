from django import forms
from enroll.models import User

class CustomerDetails(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'Address':forms.TextInput(attrs={'class':'form-control'}),
            'contact':forms.TextInput(attrs={'class':'form-control'}),
            'Delivery_date':forms.DateTimeInput(attrs={'class':'form-control'}),
        }


