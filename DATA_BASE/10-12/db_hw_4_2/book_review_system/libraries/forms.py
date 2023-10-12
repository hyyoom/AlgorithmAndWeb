from .models import Book,Review
from django import forms



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('__all__')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('__all__')




