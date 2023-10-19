from django.urls import path
from . import views


urlpatterns = [
    path('musics/',views.music_list),
    path('musics/<int:music_pk>/',views.music_detail),
    path('musics/<int:music_pk>/comment/',views.comment_create),
    path('comment/', views.comment_list),
    path('comment/<int:comment_pk>', views.comment_detail),
]