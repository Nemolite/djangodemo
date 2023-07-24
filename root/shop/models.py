from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100,db_index=True, verbose_name='Категория')
    description = models.CharField(max_length=255, verbose_name='Описание категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'  # Изменение назавния модели в админке
        verbose_name_plural = 'Категории'  # Что бы корректно отображалось множественное число
        ordering = ['name']  # Сортировка по времени создания и после по имени

    def get_absolute_url(self):
        return f'/category/{self.id}/'

class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Товар')
    description = models.CharField(max_length=255, verbose_name='Описание товара')
    country = models.CharField(max_length=50, verbose_name='Страна производитель')
    image = models.ImageField(upload_to='images', verbose_name='Изображение товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость товара')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество товара')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'  # Изменение назавния модели в админке
        verbose_name_plural = 'Продукты'  # Что бы корректно отображалось множественное число
        ordering = ['name']  # Сортировка по времени создания и после по имени

    def get_absolute_url(self):
        return f'/product/{self.id}/'

    def get_addproduct_url(self):
        return f'/addproduct/{self.id}/'
