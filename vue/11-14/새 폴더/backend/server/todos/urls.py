from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # 할일 전체 목록 가져오기
    path('todos/', views.todos ),
]
