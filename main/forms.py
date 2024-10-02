from main.models import tokocamera
from django import forms

class tokocameraform(forms.ModelForm):
    class Meta:
        model = tokocamera
        fields = ['name', 'price', 'description', 'stock']