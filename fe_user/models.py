from django.db import models


# Create your models here.


class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upasswd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=30)
    uphone = models.CharField(max_length=11)
    uaddress = models.CharField(max_length=60)
