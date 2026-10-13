from django.contrib import admin


from apps.product.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    search_fields = ('name', 'description')
    list_filter = ('category', 'tags')
    filter_horizontal = ('tags',)
