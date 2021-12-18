
from django.contrib import admin
from .models import Product, Category
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('rating', 'rating_counter')
    list_display = (
        'name',
        'category',
        'style',
        'color',
        'price',
        'sale',
        'sale_price',
        'item_count',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
