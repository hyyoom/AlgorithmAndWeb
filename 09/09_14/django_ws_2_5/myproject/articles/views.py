from django.shortcuts import render

# Create your views here.

def index(r):
    return render(r,'articles/index.html')