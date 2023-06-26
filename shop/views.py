import copy

from django.db.models import RestrictedError
from django.shortcuts import render, redirect

from shop.models import Product, Category


def products_view(request):
    product = Product.objects.all()
    return render(request, "home.html", {'products': product})


def product_view(request, *args, **kwargs):
    if not "Delete" in request.path.title():
        product = Product.objects.get(pk=kwargs["id"])
        return render(request, "product.html", {'product': product})
    else:
        try:
            Product.objects.get(pk=kwargs['id']).delete()
            return redirect('home')
        except RestrictedError:
            return redirect('home')


def product_edit_view(request, *args, **kwargs):
    if request.method == "GET":
        product = Product.objects.get(pk=kwargs['id'])
        categories = Category.objects.all()
        product.price_coast = str(product.price_coast)
        return render(request, "product_edit.html", {'product': product, 'categories': categories})
    else:
        Product.objects.filter(pk=kwargs['id']).update(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            select_id=request.POST.get('category'),
            price_coast=float(request.POST.get('price')),
            pic_img=request.POST.get('pic_img'))
        return redirect('home')


def category_add_view(request):
    if request.method == "GET":
        return render(request, "category_add.html")
    else:
        Category.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description')
        )
        return redirect("home")


def product_add_view(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, "product_add.html", {'categories': categories})
    else:
        Product.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            price_coast=request.POST.get('price'),
            pic_img=request.POST.get('pic_img'),
            select_id=request.POST.get('category'),
        )
        return redirect("home")


def categories_view(request, *args, **kwargs):
    if not kwargs:
        categories = Category.objects.all().order_by('id')
        return render(request, "categories.html", {'categories': categories})
    else:
        try:
            Category.objects.get(pk=kwargs['id']).delete()
            return redirect('categories')
        except RestrictedError:
            return redirect('categories')


def category_edit_view(request, *args, **kwargs):
    if request.method == "GET":
        category = Category.objects.get(pk=kwargs['id'])
        return render(request, "category_edit.html", {'category': category})
    else:
        Category.objects.filter(pk=kwargs['id']).update(title=request.POST.get('title'),
                                                        description=request.POST.get('description'))
        return redirect('categories')
