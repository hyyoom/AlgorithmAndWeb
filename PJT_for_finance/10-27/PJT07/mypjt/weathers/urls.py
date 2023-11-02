from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    # 1. 날씨 api테스트
    # 2. 서울 5일치 예보 데이터 확인
    # 3. 예보 데이터 중 원하는 데이터만 db에 저장
    # 4. 저장된 데이터 전체 조회
    # 5. 특정 조건 데이터 확인
    path('index/', views.index),
    path('save-data/', views.save_data),
    path('list-data/', views.list_data),
    path('hot_weathers/', views.hot_weathers),
]
