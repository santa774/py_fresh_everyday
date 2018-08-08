# coding: utf-8
from django.shortcuts import render
from django.core.paginator import Paginator
from models import *


# Create your views here.
def index(request):
    type_list = TypeInfo.objects.all()
    type0 = type_list[0].goodsinfo_set.order_by('-id')[0:4]
    type01 = type_list[0].goodsinfo_set.order_by('-gclick')[0:4]
    type1 = type_list[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = type_list[1].goodsinfo_set.order_by('-gclick')[0:4]
    type2 = type_list[2].goodsinfo_set.order_by('-id')[0:4]
    type21 = type_list[2].goodsinfo_set.order_by('-gclick')[0:4]
    type3 = type_list[3].goodsinfo_set.order_by('-id')[0:4]
    type31 = type_list[3].goodsinfo_set.order_by('-gclick')[0:4]
    type4 = type_list[4].goodsinfo_set.order_by('-id')[0:4]
    type41 = type_list[4].goodsinfo_set.order_by('-gclick')[0:4]
    type5 = type_list[5].goodsinfo_set.order_by('-id')[0:4]
    type51 = type_list[5].goodsinfo_set.order_by('-gclick')[0:4]
    context = {
        'title': '首页',
        'shop_cart': 1,
        'typelist': type_list,
        'type0': type0, 'type01': type01,
        'type1': type1, 'type11': type11,
        'type2': type2, 'type21': type21,
        'type3': type3, 'type31': type31,
        'type4': type4, 'type41': type41,
        'type5': type5, 'type51': type51
    }
    return render(request, 'fe_goods/index.html', context)


def cart(request):
    context = {
        'title': '购物车',
        'sub_page': 1,
        'sub_page_name': '购物车'
    }
    return render(request, 'fe_goods/cart.html', context)


def detail(request):
    context = {
        'title': '商品详情',
        'shop_cart': 1,
    }
    return render(request, 'fe_goods/detail.html', context)


def goods_list(request, type_id, sort_type, page_index):
    typeinfo = TypeInfo.objects.get(tid=type_id)
    recommend_list = typeinfo.goodsinfo_set.order_by('-id')[0:2]
    if sort_type == '1':
        glist = GoodsInfo.objects.filter(gtype=type_id).order_by('-id')
    elif sort_type == '2':
        glist = GoodsInfo.objects.filter(gtype=type_id).order_by('-gprice')
    elif sort_type == '3':
        glist = GoodsInfo.objects.filter(gtype=type_id).order_by('-gclick')

    goods_paginator = Paginator(glist, 10)
    page = goods_paginator.page(int(page_index))
    context = {
        'title': '商品列表',
        'shop_cart': 1,
        'recommend_list': recommend_list,
        'goods_list': page.object_list,
        'plist': goods_paginator.page_range,
    }
    return render(request, 'fe_goods/list.html', context)
