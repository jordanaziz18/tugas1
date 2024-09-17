from main.models import tokocamera
from django import forms

class tokocameraform(forms.ModelForm):
    class Meta:
        model = tokocamera
        fields = '__all__'