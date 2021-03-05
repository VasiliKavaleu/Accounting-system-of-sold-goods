from django.db import models


class Category(models.Model):
    name = models.CharField('Название категории', max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField('Название магазина', max_length=200, db_index=True)

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return self.name


class Storage(models.Model):
    name = models.CharField('Название склада', max_length=200, db_index=True)

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('Название товара', max_length=200, db_index=True)
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    shop = models.ManyToManyField(Shop)
    storage = models.ManyToManyField(Storage)
    description = models.TextField('Описание', blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    sold = models.BooleanField('Продан', default=False)
    created = models.DateTimeField('Создан', auto_now_add=True)
    updated = models.DateTimeField('Обновлен', auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

