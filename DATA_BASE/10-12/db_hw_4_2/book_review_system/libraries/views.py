from django.shortcuts import render,redirect
from .forms import BookForm, ReviewForm
from .models import Book,Review


# Create your views here.
def index(request):
    Books = Book.objects.all()
    context = {
        'Books' : Books,
    }
    return render(request, 'libraries/index.html', context)


def detail(request, pk):
    book = Book.objects.get(pk=pk)
    reviews = book.review_set.all()
    review_form = ReviewForm()
    context = {
        'reviews' : reviews,
        'review_form' : review_form,
        'book': book,
    }
    return render(request, 'libraries/detail.html', context)