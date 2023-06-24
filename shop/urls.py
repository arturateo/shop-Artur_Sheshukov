from django.urls import path
from shop.views import products_view, product_view, category_add_view, product_add_view

urlpatterns = [
    path('', products_view, name='home'),
    path('products/', products_view, name='products'),
    path('products/<int:id>/', product_view, name='product'),
    path('categories/add/', category_add_view, name='category_add'),
    path('products/add/', product_add_view, name='product_add'),
]
