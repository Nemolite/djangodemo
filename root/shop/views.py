from django.http import HttpResponseNotFound
from django.views.decorators.http import require_POST
# from cart.forms import CartAddProductForm
from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from .forms import OrderCreateForm

from .models import *


def index(request):
    product = Product.objects.all()
    product_quantity = {}
    for p in product:
        product_quantity[p.id] = [(i, str(i)) for i in range(1, p.quantity+1)]

    category = Category.objects.all()
    context = {
        'product': product,
        'category': category,
        'product_quantity':product_quantity
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
    product_quantity_choices = [(i, str(i)) for i in range(1, product.quantity+1)]
    context = {
        'product': product,
        'product_quantity_choices':product_quantity_choices
    }
    return render(request,'shop/product.html',context=context)

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = request.POST.get("quantity")
    cart.add(product=product,quantity=quantity)
    url =  '/product/' + str(product_id) + '/'
    return redirect(url)

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart')


def cart(request):
    cartproduct = Cart(request)
    context = {
        'cartproduct': cartproduct
    }
    return render(request, 'shop/cart.html', context=context)

def delete_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart')

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return render(request, 'shop/created.html',{'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'shop/create.html',
                  {'cart': cart, 'form': form})
