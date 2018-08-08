from django.contrib import admin
from models import *


# Register your models here.
class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'tid', 'tname', 'tclass']


class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'gname', 'gdesc', 'gcontent', 'gimage', 'gprice', 'gunit', 'gtype', 'gclick', 'gadv']
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 10
    fields = ['gname', 'gdesc', 'gcontent', 'gimage', 'gprice', 'gunit', 'gtype', 'gclick', 'gadv']


admin.site.register(TypeInfo, TypeInfoAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)
