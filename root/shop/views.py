from django.http import HttpResponseNotFound
from django.views.decorators.http import require_POST
# from cart.forms import CartAddProductForm
from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from .forms import CartAddProductForm

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

# Страница о нас
def onas(request):
    product = Product.objects.all().order_by("-created")[:5]
    context = {
        'product': product,
    }
    return render(request, 'shop/onas.html', context=context)

# Для 404 ошибки
def pageNotFound(request,exception):
    return  HttpResponseNotFound("<h1>Страница не найдена</h1>")

# Страница показа одного товара
def product(request, id):
    product = get_object_or_404(Product,id=id)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request,'shop/product.html',context=context)

@require_POST
def cart_add(request, product_id):
    # Инициализация корзины через конструктор
    cart = Cart(request)
    # Получение товара по id
    product = get_object_or_404(Product, id=product_id)
    # Получение данных с формы
    form = CartAddProductForm(request.POST)
    # Валидция элементов формы
    if form.is_valid():
        # Доступ к чистым данным
        cd = form.cleaned_data
        # Используем метод add для добавления товара в корзину
        # Первый параметр - товар
        # Второ параметр - количество
        # Третий параметр - False
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    return redirect('onas')


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart')


def cart(request):
    cart = Cart(request)
    print(cart)
    # for item in cart:
    #     item['update_quantity_form'] = CartAddProductForm(initial={
    #                         'quantity': item['quantity'],
    #                         'override': True})
    context = {
        'cartproduct': cart
    }
    return render(request, 'shop/cart.html', context=context)
