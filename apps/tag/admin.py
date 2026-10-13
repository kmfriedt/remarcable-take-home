from django.contrib import admin

from apps.tag.models import Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)
    ordering = ('name',) # Not sure I would do this in production may slow down admin page