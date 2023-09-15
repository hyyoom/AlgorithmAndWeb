from django.urls import path
from . import views

# name==html에서 url쓸때 namespace(app_name):name
# 다른 app에서도 throw, catch같은 이름의 기능이 있을수 있기에, 구분을 위해 씀
app_name = 'articles'
urlpatterns = [
    # 사용자가 서버로 데이터를 전달하기 위한 화면 보여줘
    path('throw/', views.throw, name='throw'),
    # name==html에서 url쓸때 articels:name

    # 사용자가 서버로 전달한 데이터를 받아서 그린 화면 응답 
    path('catch/', views.catch, name='catch'),


    #사용자가 입력할 수 있는 화면 제공,
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]
