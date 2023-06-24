from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Наименование', unique=True)
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        db_table = 'category'
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Product(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Наименование')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    select = models.ForeignKey("shop.Category", on_delete=models.RESTRICT,
                               verbose_name="Категория", related_name='category')
    create_date_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    price_coast = models.DecimalField(null=False, blank=False, max_digits=1000,
                                      decimal_places=2, verbose_name='Цена товара')
    pic_img = models.CharField(max_length=500, null=False, blank=False, verbose_name='Изображение товара')

    def __str__(self):
        return f'{self.title} - {self.description} - {self.select} - {self.create_date_time} - ' \
               f'{self.price_coast} - {self.pic_img}'

    class Meta:
        db_table = 'product'
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
