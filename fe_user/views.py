# coding: utf-8
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from models import *
from hashlib import sha1


# Create your views here.


def index(request):
    return render(request, 'fe_user/../templates/fe_goods/index.html')


def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 0, 'uname': uname}
    return render(request, 'fe_user/login.html', context)


def info(request):
    user = UserInfo.objects.get(id=request.session.get('user_id'))
    context = {'title': '个人信息', 'uname': user.uname, 'uphone': user.uphone, 'uaddress': user.uaddress}
    return render(request, 'fe_user/user_center_info.html', context)


def order(request):
    context = {'title': '全部订单'}
    return render(request, 'fe_user/user_center_order.html', context)


def site(request):
    user = UserInfo.objects.get(id=request.session.get('user_id'))
    if request.method == 'POST':
        post = request.POST
        user.ushou_name = post.get('ushou_name')
        user.uaddress = post.get('uaddress')
        user.uyoubian = post.get('uyoubian')
        user.uphone = post.get('uphone')
        user.save()
    context = {'title': '收货地址', 'user': user}
    return render(request, 'fe_user/user_center_site.html', context)


def register(request):
    context = {'title': '用户注册'}
    return render(request, 'fe_user/register.html', context)


def register_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count': count})


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
    save_name = post.get('save_name', 0)

    users = UserInfo.objects.filter(uname=username)
    if len(users) != 0:
        s1 = sha1()
        s1.update(pwd)
        if s1.hexdigest() == users[0].upasswd:
            # 用户名密码都匹配，调转到用户信息界面
            http_redirect = HttpResponseRedirect('/goods/index')
            if save_name != 0:
                http_redirect.set_cookie('uname', username)
            else:
                http_redirect.set_cookie('uname', '', max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['user_name'] = users[0].uname
            return http_redirect
        else:
            # 用户名正确，密码错误，提示对应的信息
            context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 1, 'uname': username}
            return render(request, 'fe_user/login.html', context)
    else:
        context = {'title': '用户登录', 'error_name': 1, 'error_pwd': 0, 'uname': username}
        return render(request, 'fe_user/login.html', context)
