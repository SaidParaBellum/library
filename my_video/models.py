from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Video(models.Model):
    name = models.CharField('Name', max_length=100)
    date_time = models.DateTimeField('Date_time', null=True)
    video_file = models.FileField('video_file', null=True, blank=True, upload_to='video_files/',
                                 validators=[FileExtensionValidator(['mp4', 'MOV'])])
    created_at = models.DateTimeField('Created_at', auto_now_add=True)



User = get_user_model()

class FavoriteVideo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_videos')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='favorited_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'video')

    def __str__(self):
        return f"{self.user.username} -> {self.video.name}"