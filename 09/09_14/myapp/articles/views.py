from django.shortcuts import render
from .models import Article
# Create your views here.
def throw(r):
    return render(r, 'articles/throw.html')

def catch(request):
    # 요청 객체에서 데이터 꺼내오기
    name = request.GET.get('name')
    context = {
        'name': name,
    }
    return render(request, 'articles/catch.html', context)

def new(request):
    # 사용자가 입력할 수 있는 화면 제공
    return render(request, 'articles/new.html')

def create(r):
    title = r.POST.get('title')
    content = r.POST.get('content')
    print(title, content)
    article = Article()
    article.title = title
    article.content = content
    article.save()

    # 사용자가 입력 한 데이터 받아서 db에 저장하고 화면 보여주기
    return render(r, 'articles/create.html')