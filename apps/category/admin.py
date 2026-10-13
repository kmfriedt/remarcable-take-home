from django.contrib import admin

from apps.category.models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)
    ordering = ('name',) # may not be a good idea in production
