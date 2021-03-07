from http.client import HTTPResponse

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Shop, Storage, Product, ProductOnStorage, SoldProduct
from .services import get_latest_news


def get_main_page(request):
    return render(request, 'main.html',
                  {
                    'data_set1': get_latest_news()[0],
                    'data_set2': get_latest_news()[1],
                  })

@login_required
def get_list_shops(request):
    """Displaying list of shops."""
    shops = Shop.objects.all()
    return render(request, 'list_shops.html', {'shops': shops})

@login_required
def get_list_storages(request):
    """Displaying list of storages."""
    storages = Storage.objects.all()
    return render(request, 'list_storages.html', {'storages': storages})

@login_required
def get_list_products(request):
    """Displaying list of available products."""
    available_products = ProductOnStorage.objects.all()
    return render(request, 'list_available_products.html', {'available_products': available_products})

@login_required
def get_list_sold_products(request):
    """Displaying list of sold products."""
    sold_products = SoldProduct.objects.all()
    return render(request, 'list_sold_products.html', {'sold_products': sold_products})

@login_required
def product_list_by_storage(request, id):
    """Displaying list of products by storage."""
    products = ProductOnStorage.objects.filter(storage__id=id)
    storage = get_object_or_404(Storage, id=id)
    return render(request, 'products_of_storage.html', {'products_of_storage': products, 'storage': storage})

@login_required
def product_list_by_shop(request, id):
    """Displaying list of products by shop."""
    products = ProductOnStorage.objects.filter(shops__id=id)
    shop = get_object_or_404(Shop, id=id)
    return render(request, 'products_of_shop.html', {'products_of_shop': products, 'shop': shop})

def get_about_page(request):
    return render(request, 'about.html')
