from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Picture(models.Model):
    name = models.CharField('Name', max_length=100)
    picture = models.ImageField('Picture', null=True, blank=True,
                                 validators=[FileExtensionValidator(['jpg', 'img'])])




User = get_user_model()

class FavoritePicture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_pictures')
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE, related_name='favorited_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'picture')

    def __str__(self):
        return f"{self.user.username} -> {self.picture.name}"