from django.shortcuts import render,redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, "articles/index.html", context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }

    return render(request, "articles/detail.html", context)


def new(request):
    return render(request, "articles/new.html")


def create(request):
    title = request.POST.get('title')
    content = request.POST.get("content")
    #1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    #2 유효성 검사를 위해서 2번을 사용할거임 앞으로..
    article = Article(title=title, content=content)
    article.save()

    #3
    # Article.objects.create(title=title, content=content)
    return redirect('articles:index')


def delete(request,pk):
    # 몇번 게시글 삭제할것인지 조회
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect("articles:index")


def edit(request,pk):
    article = Article.objects.get(pk=pk)
    

    return render(request, "articles/edit/")



