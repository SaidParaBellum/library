from django import forms

from my_pictures.models import Picture


class PictureCreateForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['name', 'picture']

