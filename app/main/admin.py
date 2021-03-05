from django.contrib import admin

from .models import Storage, Shop, Category, Product


admin.site.register(Storage)
admin.site.register(Shop)
admin.site.register(Category)
admin.site.register(Product)
