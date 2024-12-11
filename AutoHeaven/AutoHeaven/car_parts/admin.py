from django.contrib import admin
from .models import CarPart

@admin.register(CarPart)
class CarPartAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'owner', 'image_display')  # Fields to display in list view
    list_filter = ('owner', 'price')  # Filters for the sidebar
    search_fields = ('name', 'description')  # Fields to search
    readonly_fields = ('image_display',)  # Make the image preview non-editable in the admin form
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'price', 'owner', 'image', 'image_display'),
        }),
    )

    def image_display(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" height="100" style="object-fit: cover;" />'
        return "No image"
    image_display.allow_tags = True
    image_display.short_description = 'Image Preview'
