from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.TextField(max_length=20)
    old = models.CharField(max_length=2, default='나이를 입력해 주세요.')
    email = models.TextField(max_length=30, default='이메일을 입력해 주세요.')