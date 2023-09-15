from django.db import models

# Create your models here.
# 내가 app에서 사용할 데이터 정의

# 게시판의 게시글 : 제목, 내용
class Article(models.Model): 
    #이미 model의 클래스를 장고가 만들어놔서 필요 데이터만
    #정의하면 됨. models.Model클래스
    #사용할 값 이름 = 자료형
    title = models.CharField(max_length=10)
    content = models.TextField()
    pass