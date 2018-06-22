from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'fe_goods/index.html', '')


def cart(request):
    return render(request, 'fe_goods/cart.html', '')
