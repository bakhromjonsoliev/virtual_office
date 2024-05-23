from django import forms
from .models import Murojaat

class MurojaatForm(forms.ModelForm):
    class Meta:
        model = Murojaat
        fields = ['fish', 'ish_joyi', 'telefon', 'email', 'hudud']
