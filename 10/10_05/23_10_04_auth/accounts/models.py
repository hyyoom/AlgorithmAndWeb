from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 이 클래스를 이용해서 인증할건데...
# 기본 기능은 장고가 이미 다 구현해 뒀습니다. >> AbstractUser
# 장고한테..앞으로 인증할 때 내가 만든 User 클래스 쓸거라고 알려줘야 합니다. 
class User(AbstractUser):
    pass