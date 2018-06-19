# coding: utf-8
from django.db import models


# Create your models here.


class UserInfoManager(models.Manager):
    def create_user(self, uname, upasswd, uemail):
        user = self.create(uname=uname, upasswd=upasswd, uemail=uemail)
        return user


class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upasswd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=30)
    uphone = models.CharField(max_length=11, default='')
    uaddress = models.CharField(max_length=60, default='')
    ushou_name = models.CharField(max_length=20, default='')
    uyoubian = models.CharField(max_length=10, default='')
    objects = UserInfoManager()
