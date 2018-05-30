from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(AbstractUser):
    """
    用户表
    """
    userid =models.CharField(max_length=10,verbose_name="用户ID",help_text="用户ID")
    mobile = models.CharField(max_length=11, verbose_name="电话", help_text="电话号码")
    nickname = models.CharField(max_length=10, verbose_name="用户昵称", help_text="用户昵称")


    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.mobile
