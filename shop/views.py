from django.db.models import RestrictedError
from django.shortcuts import render, redirect, get_object_or_404

from shop.models import Product, Category


def products_view(request):
    product = Product.objects.all()
    return render(request, "home.html", {'products': product})


def product_view(request, *args, **kwargs):
    product = Product.objects.get(pk=kwargs["id"])
    return render(request, "product.html", {'product': product})


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
