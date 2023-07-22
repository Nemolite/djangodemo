from django.contrib import admin

from .models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description', 'country', 'image', 'price', 'quantity', 'quantity')
    list_display_links = ('id', 'name')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)