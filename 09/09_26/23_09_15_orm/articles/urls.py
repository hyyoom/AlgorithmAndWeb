from django.urls import path
from . import views
app_name='articles'
urlpatterns = [
    # index, new, create, delete
    path('index/',views.index, name='index'),
    # path('new/',views.new, name='new'),
    path('create/',views.create, name='create'),
    path('delete/<int:pk>/',views.delete, name='delete'),
    #상세 페이지 /articles/1/
    path('<int:pk>', views.detail, name="detail"),
    # path('edit/<int:pk>/', views.edit, name='edit'),
    #수정 페이지

    #수정해서 db에 변경된거 저장하세열
    path('update/<int:pk>/', views.update, name='update'),
]