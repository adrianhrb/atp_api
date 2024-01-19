from django import forms


class FileLoaderForm(forms.Form):
    match = forms.FileField(required=False)
    players = forms.FileField(required=False)
    stats = forms.FileField(required=False)
