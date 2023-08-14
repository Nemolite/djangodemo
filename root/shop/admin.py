from django.contrib import admin
from .models import Orders, OrderItem
from .models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description', 'country', 'image', 'price', 'quantity', 'quantity')
    list_display_links = ('id', 'name')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
    'address', 'paid','created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]