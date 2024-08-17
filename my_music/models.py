from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Music(models.Model):
    name = models.CharField('Name', max_length=100)
    year = models.IntegerField('Year')
    music_file = models.FileField('music_file', null=True, blank=True, upload_to='music_files/',
                                 validators=[FileExtensionValidator(['mp3'])])
    created_at = models.DateTimeField('Created_at', auto_now_add=True)




User = get_user_model()

class FavoriteMusic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_music')
    music = models.ForeignKey(Music, on_delete=models.CASCADE, related_name='favorited_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'music')

    def __str__(self):
        return f"{self.user.username} -> {self.music.name}"