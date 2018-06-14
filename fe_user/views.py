# coding: utf-8
from django.shortcuts import render, redirect
from django.http import JsonResponse
from models import *
from hashlib import sha1


# Create your views here.


def index(request):
    return render(request, 'fe_user/index.html')


def login(request):
    return render(request, 'fe_user/login.html', "")


def register(request):
    return render(request, 'fe_user/register.html', "")


def register_exist(request):
    uname = request.GET().get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count', count})


def register_handler(request):
    # 获取用户填写的信息
    post = request.POST
    user_name = post.get('user_name')
    pwd = post.get('pwd')
    cpwd = post.get('cpwd')
    email = post.get('email')
    allow = post.get('allow')
    # 检查两次输入的密码是否一致
    if pwd != cpwd or user_name == u'' or pwd == u'' or cpwd == u'' or email == u'':
        return redirect('/user/register')
    # 密码加密
    s1 = sha1()
    s1.update(pwd)
    hex_pwd = s1.hexdigest()
    # 保存用户到数据库并调转页面
    UserInfo.objects.create_user(user_name, hex_pwd, email)
    return redirect('/user/login')


def login_handler(request):
    # 获取用户填写的信息
    post = request.POST
    username = post.get('username')
    pwd = post.get('pwd')
    s1 = sha1()
    s1.update(pwd)
    hex_pwd = s1.hexdigest
    # 检查数据库是否存在此用户
    result = UserInfo.objects.filter(uname=username, upasswd=hex_pwd)
    if len(result) == 0:
        return redirect('/user/login')

    return redirect('/user/register')
