from django.shortcuts import render, redirect
from .models import Article
# 모델 밑에있는 알티클클래스를 사용한다.

# Create your views here.

def index(request):
    # 게시글 목록 조회해서 템플릿에 전달
    # 게시글 목록 데이터 베이스에서 조회
    # ORM 이용해야 하는데 >> model이 이 역할을 함
    articles = Article.objects.all()
    context={
        'articles' : articles
    }
    return render(request, 'articles/index.html/', context)

def new(request):
    return render(request, 'articles/new.html/')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article(title=title,content=content)
    article.save()

    # articles = Article.objects.all()
    # context = {
    #     'articles' : articles
    # }
    # 요청에서 데이터 받아와서 db에 저장하고
    # 목록조회해서 인덱스 템플릿에 전달
    return redirect('articles:index')

def delete(request,pk):
    # db에서 삭제하고 목록조회해서 템플릿에 전달
    # record 단위는 instance로 처리..
    article = Article.objects.get(pk=pk)
    article.delete()

    # articles = Article.objects.all()
    # context = {
    #     'articles' : articles
    # }
    return redirect('articles:index')

