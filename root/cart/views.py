from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


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
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
                            'quantity': item['quantity'],
                            'override': True})
    return render(request, 'cart/cart.html', {'cart': cart})
