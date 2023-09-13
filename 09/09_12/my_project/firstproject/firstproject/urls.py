"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from articles import views


# django가 어떤 요청을 처리할지 목록 작성
# 1. hello/ 요청 처리하기
# 2. application에 있는 views.py import하기

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hello/', views.hello),
    path('input/', views.name_form ), #이름입력 화면 요청
    path('greeting/', views.hello) #사용자가 전달한 이름을 받아서 인사하는 화면 보여주기

]
