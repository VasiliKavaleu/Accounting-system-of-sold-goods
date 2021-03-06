from django.db import models


class Category(models.Model):
    objects = None
    name = models.CharField('Название категории', max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('Название товара', max_length=200, db_index=True)
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 null=True,
                                 on_delete=models.SET_NULL)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField('Название магазина', max_length=200, db_index=True)
    product = models.ManyToManyField(Product, verbose_name='Товары')

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


class ProductOnStorage(models.Model):
    product = models.ForeignKey(Product,
                                verbose_name='Товар',
                                related_name='products',
                                on_delete=models.CASCADE)
    storage = models.ForeignKey(Storage,
                                verbose_name='Склад',
                                related_name='products',
                                on_delete=models.CASCADE)
    available = models.BooleanField('Наличие на складе', default=False)

    class Meta:
        verbose_name = 'Наличие товара на складе'
        verbose_name_plural = 'Наличие товаров на складе'

    def __str__(self):
        return self.product.name


class SoldProduct(models.Model):
    name = models.ForeignKey(Product,
                             related_name='sold_products',
                             null=True,
                             on_delete=models.SET_NULL)
    shop = models.ForeignKey(Shop,
                             related_name='sold_products',
                             null=True,
                             on_delete=models.SET_NULL)
    storage = models.ForeignKey(Storage,
                                related_name='sold_products',
                                null=True,
                                on_delete=models.SET_NULL)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Проданный товар'
        verbose_name_plural = 'Проданные товары'

    def __str__(self):
        return self.name
