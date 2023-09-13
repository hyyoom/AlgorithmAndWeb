from django.urls import path
from . import views
# from articles import views
# from movies import views as movies_views

app_name = 'movies'

urlpatterns = [
    path('index/', views.movies, name='index'),
    path('page1/', views.movies, name='page1'),
    path('page2/', views.movies, name='page2'),
]
