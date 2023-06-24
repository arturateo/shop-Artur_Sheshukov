from django.shortcuts import render

from shop.models import Product


def products_view(request):
    product = Product.objects.all()
    return render(request, "home.html", {'products': product})


def product_view(request):
    return render(request, "home.html")


def category_add_view(request):
    return render(request, "category_add.html")


def product_add_view(request):
    return render(request, "product_add.html")
