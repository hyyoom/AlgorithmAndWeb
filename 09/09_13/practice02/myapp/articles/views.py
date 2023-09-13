from django.shortcuts import render

# Create your views here.

def index(r):
    context = {
        'name':"눌렀냐?"
    }
    return render(r, "articles/index.html", context)

def catch(r, name,number):
    context = {
        'name' : name,
        'number' : number,
    }
    return render(r, "articles/catch.html", context)