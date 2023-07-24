from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from .models import *


def index(request):
    product = Product.objects.all()
    category = Category.objects.all()
    context = {
        'product': product,
        'category': category,
    }
    return render(request, 'shop/index.html', context=context )

def category(request,id):
    product = Product.objects.filter(category=id)
    category = Category.objects.all()
    context = {
        'product': product,
        'category': category,
    }

    return render(request,'shop/index.html',context=context)

def product(request,id):
    product = Product.objects.filter(id=id)
    context = {
        'product': product,
    }

    return render(request,'shop/product.html',context=context)

def addproduct(request,id):
    return render(request, 'shop/cart.html')

def onas(request):
    product = Product.objects.all().order_by("-created")[:5]
    context = {
        'product': product,
    }
    return render(request, 'shop/onas.html', context=context)

# Для 404 ошибки
def pageNotFound(request,exception):
    return  HttpResponseNotFound("<h1>Страница не найдена</h1>")
