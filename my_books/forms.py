from django import forms

from my_books.models import Book


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'year']

