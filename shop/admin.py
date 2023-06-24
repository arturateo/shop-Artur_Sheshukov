from django.contrib import admin

from shop.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    list_display_links = ['id', 'title', 'description']
    list_filter = ['title']
    search_fields = ['title', 'description']
    fields = ['title', 'description']


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'select', 'create_date_time', 'price_coast', 'pic_img']
    list_filter = ['title', 'description', 'select']
    list_display_links = ['id', 'title', 'description']
    search_fields = ['title', 'description', 'category']
    fields = ['title', 'description', 'select', 'price_coast', 'pic_img']


admin.site.register(Product, ProductAdmin)
