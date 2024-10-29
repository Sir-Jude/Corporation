from django import forms
from .models import Corporation


class CorporationForm(forms.ModelForm):
    class Meta:
        model = Corporation
        fields = (
            "corporation_name",
            "sector",
            "address",
            "phone_number",
            "email",
            "url",
            "linkedin",
        )
    
        widgets = {
            "corporation_name": forms.TextInput(attrs={"class": "form-control"}),
            "sector": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "url": forms.URLInput(attrs={"class": "form-control"}),
            "linkedin": forms.URLInput(attrs={"class": "form-control"}),
        }
    
    def save(self, commit=True):
        # Save corporation instance first
        corporation = super().save(commit=False)
        
        if commit:
            corporation.save()
            
        return corporation