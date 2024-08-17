from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Book(models.Model):
    name = models.CharField('Name', max_length=100)
    year = models.IntegerField('Year')
    description = models.TextField('Description', max_length=150)
    num_pages = models.IntegerField("Pages")
    author = models.CharField('Author', max_length=70)
    book_file = models.FileField('Book_file', null=True,  blank=True,
                                 validators=[FileExtensionValidator(['pdf'])] )



User = get_user_model()

class FavoriteBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_books')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='favorited_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book')

    def __str__(self):
        return f"{self.user.username} -> {self.book.name}"