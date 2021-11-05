from django.contrib import admin
from catalog.models import Product, Category
from django.utils.html import format_html

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'price',
        'quantity',
        'status',
        'sort_order',
        'image_tag'
    )

    def image_tag(self,obj):
        tag_image = '<img src="{0}" style="width: 45px; height:45px;" />'.format(obj.image.url)
        return format_html(tag_image)

    list_filter = ('status', 'categories')
    search_fields = ('sku', 'name')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
