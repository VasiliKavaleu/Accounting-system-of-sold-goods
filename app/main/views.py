from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .models import Shop, Storage, Product
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
    available_products = Product.objects.filter(sold=False)
    return render(request, 'list_available_products.html', {'available_products': available_products})

@login_required
def get_list_sold_products(request):
    """Displaying list of sold products."""
    sold_products = Product.objects.filter(sold=True)
    return render(request, 'list_sold_products.html', {'sold_products': sold_products})

@login_required
def product_list_by_storage(request, id):
    """Displaying list of products by storage."""
    storage = None
    storages = Storage.objects.all()
    products = Product.objects.all()
    if id:
        storage = get_object_or_404(Storage, id=id)
        products = products.filter(storage=storage, sold=False)
    return render(request, 'products_of_storage.html', {'products_of_storage': products, 'storage': storage})

@login_required
def product_list_by_shop(request, id):
    """Displaying list of products by shop."""
    shop = None
    shops = Shop.objects.all()
    products = Product.objects.all()
    if id:
        shop = get_object_or_404(Shop, id=id)
        products = products.filter(shop=shop, sold=False)
    return render(request, 'products_of_shop.html', {'products_of_shop': products, 'shop': shop})


