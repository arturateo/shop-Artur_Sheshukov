from django.shortcuts import render

from shop.models import Product


def products_view(request):
    product = Product.objects.all()
    return render(request, "home.html", {'products': product})


def product_view(request, *args, **kwargs):
    product = Product.objects.get(pk=kwargs["id"])
    return render(request, "product.html", {'product': product})


def category_add_view(request):
    return render(request, "category_add.html")


def product_add_view(request):
    return render(request, "product_add.html")
