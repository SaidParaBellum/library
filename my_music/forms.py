from django import forms

from my_music.models import Music


class MusicCreateForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['name', 'year', 'music_file']

