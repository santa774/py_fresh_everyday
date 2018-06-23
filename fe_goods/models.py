from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class TypeInfo(models.Model):
    tname = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)


class GoodsInfo(models.Model):
    gname = models.CharField(max_length=20)
    gdesc = models.CharField(max_length=100)
    gcontent = HTMLField()
    gimage = models.ImageField(upload_to='fe_goods')
    gprice = models.DecimalField(decimal_places=2, max_digits=5)
    gunit = models.CharField(max_length=20, default='500g')
    gtype = models.ForeignKey(TypeInfo)
    gclick = models.IntegerField(default=0)
    gadv = models.BooleanField(default=False)
    isDelete = models.BooleanField(default=False)
