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
        if product_id not in self.cart:
            total_product_price = product.price * int(quantity)
            self.cart[product_id] = {'quantity': quantity,
                                     'price': str(product.price),
                                     'total_product_price':str(total_product_price)}
        else:
            total_product_price = Decimal(self.cart[product_id]['total_product_price'])
            cart_quantity = self.cart[product_id]['quantity']
            cart_quantity = int(cart_quantity) + int(quantity)
            total_product_price = total_product_price + product.price * int(quantity)
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
            item['total_product_price'] = Decimal(item['total_product_price'])
            yield item

    def __len__(self):
        # Подсчитать все товарные позиции в корзине
        return sum(int(item['quantity']) for item in self.cart.values())

    def clear(self):
        # удалить корзину из сеанса
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def get_total_price(self):
        return sum(Decimal(item['total_product_price']) for item in self.cart.values())