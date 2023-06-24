from django.shortcuts import render, redirect

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
