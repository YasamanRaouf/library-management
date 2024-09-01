from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'publication_date']


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=200)
