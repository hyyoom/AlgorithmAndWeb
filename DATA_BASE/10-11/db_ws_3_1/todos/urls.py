from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('delete/<pk>', views.delete, name='delete'),
    path('todo_complete/<pk>', views.todo_complete, name='todo_complete'),
]
