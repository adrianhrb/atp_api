from django import forms
from .models import Match

class MatchAI(forms.Form):
    match = forms.ModelChoiceField(queryset=Match.objects.all())