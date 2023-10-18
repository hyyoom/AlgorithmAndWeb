from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    #symmetrical 대칭 할거냐 1->2 데이터 생기면 2->1생겨버림 -> 자동 맞팔됨..
    #기본값이 true라 false로 넣어줌.
