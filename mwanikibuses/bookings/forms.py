from django import forms
from .models import tester

class testing(forms.ModelForm):
    class meta:
        model = tester
        fields = ['name', 'integer']