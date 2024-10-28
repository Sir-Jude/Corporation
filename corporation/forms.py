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
            "linkedin"
        )
    
    def save(self, commit=True):
        # Save corporation instance first
        corporation = super().save(commit=False)
        
        if commit:
            corporation.save()
            
        return corporation