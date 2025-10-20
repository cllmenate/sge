from django.contrib import admin
from products import models


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'brand',
        'category',
        'serial_number',
        'quantity',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'title',
        'brand__name',
        'category__name',
        'serial_number',
    )
    list_filter = ('created_at', 'updated_at',)


admin.site.register(models.Product, ProductAdmin)
