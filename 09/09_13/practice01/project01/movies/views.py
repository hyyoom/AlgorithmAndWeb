from django.shortcuts import render

# Create your views here.
def movies(r):
    return render(r,'movies/index.html')

def page1(request):
    return render(request,'movies/page1.html')

def page2(request):
    return render(request,'movies/page2.html')