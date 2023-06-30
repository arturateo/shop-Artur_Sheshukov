from django.db.models import RestrictedError
from django.shortcuts import render, redirect, get_object_or_404

from shop.forms.category_form import CategoryForm
from shop.forms.product_form import ProductForm
from shop.models import Product, Category


def products_view(request):
    product = Product.objects.all()
    return render(request, "home.html", {'products': product})


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product.html", {'product': product})


def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        return render(request, 'delete_confirm.html', {"product": product})
    else:
        button = request.POST.get('delete')
        if button:
            product.delete()
            return redirect('home')
        return render(request, 'product.html', {"product": product})


def product_add_view(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, "product_add.html", {'form': form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, "product_add.html", {'form': form})


def product_edit_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        form = ProductForm(instance=product)
        return render(request, "product_edit.html", {'form': form, 'product': product})
    else:
        form = ProductForm(instance=product, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('product', pk=pk)
        else:
            return render(request, "product_edit.html", {'form': form, 'product': product})


def category_add_view(request):
    if request.method == "GET":
        form = CategoryForm()
        return render(request, "category_add.html", {'form': form})
    else:
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("categories")
        else:
            return render(request, "category_add.html", {'form': form})


def categories_view(request):
    categories = Category.objects.all().order_by('id')
    return render(request, "categories.html", {'categories': categories})


def category_edit_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "GET":
        form = CategoryForm(instance=category)
        return render(request, "category_edit.html", {'form': form, 'category': category})
    else:
        form = CategoryForm(instance=category, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
        else:
            return render(request, "category_edit.html", {'form': form, 'category': category})


def categories_delete_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "GET":
        return render(request, 'delete_confirm.html', {"category": category})
    else:
        button = request.POST.get('delete')
        if button:
            try:
                category.delete()
                return redirect('categories')
            except RestrictedError:
                return redirect('categories')
        return redirect('categories')
