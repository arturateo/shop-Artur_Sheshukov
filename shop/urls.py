from django.urls import path
from shop.views import products_view, product_view, category_add_view, product_add_view, categories_view, \
    category_edit_view, product_edit_view

urlpatterns = [
    path('', products_view, name='home'),
    path('products/', products_view, name='products'),
    path('product/<int:id>/', product_view, name='product'),

    path('product/<int:id>/edit/', product_edit_view, name='product_edit'),
    path('product/<int:id>/delete/', product_view, name='product_delete'),

    path('categories/add/', category_add_view, name='category_add'),
    path('products/add/', product_add_view, name='product_add'),
    path('categories/', categories_view, name='categories'),
    path('categories/<int:id>/delete/', categories_view, name='category_delete'),
    path('categories/<int:id>/edit', category_edit_view, name='category_edit'),
]
