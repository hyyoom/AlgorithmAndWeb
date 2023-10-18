from django.urls import path
from articles import views
# api/v1/articles/
# api/v1/articles/<pk>/
urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
]
