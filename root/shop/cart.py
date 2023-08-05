from decimal import Decimal
from django.conf import settings
from .models import Product
class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1):
        product_id = str(product.id)
        total_product_price = product.price
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 1,
                                     'price': str(product.price),
                                     'total_product_price':str(total_product_price)}
        else:
            cart_quantity = self.cart[product_id]['quantity']
            cart_quantity = cart_quantity + int(quantity)
            total_product_price = total_product_price + product.price
            self.cart[product_id] = {'quantity': cart_quantity,
                                     'price': str(product.price),
                                     'total_product_price': str(total_product_price)}
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        # Получаем id товаров котрые в корзине
        product_ids = self.cart.keys()
        # получить объекты product
        products = Product.objects.filter(id__in=product_ids)
        # создаем копию корзины
        cart = self.cart.copy()
        # перебираем товары
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        # Подсчитать все товарные позиции в корзине
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        # удалить корзину из сеанса
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())