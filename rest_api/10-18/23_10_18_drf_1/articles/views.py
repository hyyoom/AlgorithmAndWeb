from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article
from .serializers import ArticleListSerializer,ArticleSerializer


    # 요청이 들어오면....내가 가지고 있는
    # 게시글 목록을 문자열(JSON)로 만들어서 응답
    # DB에 있는 게시글 가져오기 : Model
    # 파이썬 객체를 JSON 문자열로 변환 : Serializer
    # DRF : Model + Serializer : ModelSerializer 짠!

@api_view(['GET','POST'])
def article_list(request):
    if request.method=='GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE']) # defatul로 GET임
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method=='GET':
    # article pk에 해당하는 게시글의 json문자열 만들기
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer = ArticleSerializer(instance=article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        # raise~ 밑에 줄 대신 해줌. 개꿀!
        # return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

