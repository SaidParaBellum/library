from django import forms

from my_video.models import Video


class VideoCreateForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['name', 'date_time', 'video_file']

