from django.shortcuts import render


# Create your views here.


def login(request):
    return render(request, 'fe_user/login.html', "")
