from django import forms

from .models import Book


class BookModelForm(forms.ModelForm):

    class Meta:
        model = Book
        exclude = ('author_post','public_date','is_no_draft','image',)
