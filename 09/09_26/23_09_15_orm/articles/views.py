from django.shortcuts import render,redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.
def index(request):
    #게시글 목록 조회해서 템플릿에 전달
    #1. 게시글 목록 DB에서 조회
    #    ORM 이용해야 하는데 >> 이 역할을 Model class(Article)가 수행
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }

    return render(request,'articles/index.html',context)

# def new(request):
#     form = ArticleForm()
#     context = {
#         'form' : form,
#     }
#     return render(request,'articles/new.html', context)




# def create(request):
#     # 요청에서 데이터 받아와서 DB에 저장하고
#     # title = request.POST.get('title')
#     # content = request.POST.get('content')
#     # Article.objects.create()
#     # article = Article(title=title,content=content)
#     # article.save()
    


#     #어떤 데이터가 들어올지 알 수 있어서 요청에서 데이터를 한꺼번에 받아올수 있음
#     form = ArticleForm(request.POST)
#     #model의 역할까지 같이. 모델의 역할 >> db에 접근
#     if form.is_valid():
#         form.save()
#         return redirect('articles:index')
#     context = {
#         'form' : form
#     }
#     return render(request, "articles/new.html", context)
#     # 정상저으로 써졌으면 목록으로 보내고
#     # 정상적으로 글 안써졌으면 글쓰기 다시 보여줌


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index') 
    else:
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request, 'articles/new.html', context)


def delete(request,pk):

    # DB에서 삭제하고 목록조회해서 템플릿에 전달
    # record 단위는 instance로 처리...
    article = Article.objects.get(pk=pk)
    article.delete()
    # articles = Article.objects.all()
    # context = {
    #     'articles' :articles
    # }
    # return render(request,'articles/index.html', context)
    return redirect('articles:index')


#상세페이지 보여달라는 요청을 처리하는 함수
def detail(request,pk):
    # DB에서 pk에 해당하는 게시글 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request,"articles/detail.html", context)


# 수정 화면 보여달라는 요청 하는 함수
# def edit(request,pk):
#     article = Article.objects.get(pk=pk)
#     context = {
#         'article' : article
#     }
#     # 수정화면 그리기
#     return render(request, 'articles/update.html', context)


# def update(request,pk):
#     article = Article.objects.get(pk=pk)
#     article.title = request.POST.get('title')
#     article.content = request.POST.get('content')
#     article.save()

#     return redirect('articles:index')

def update(request,pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("articles:detail", pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form' : form,
        'article' : article
    }
    return render(request, "articles/update.html", context)

    
    