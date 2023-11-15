from django.urls import path
from . import views


urlpatterns = [
    path('postlist/', views.postlist),
    path('categorycreate/', views.categorycreate),
]
