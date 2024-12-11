from django.contrib import admin

from AutoHeaven.cars.models.app_car import Car, CarBrand, CarModel


# Register your models here.
@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand')
    search_fields = ('model', 'brand__name')
    list_filter = ('brand',)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('owner', 'brand', 'model', 'price', 'color', 'type', 'status', 'year')
    search_fields = ('owner__username', 'brand__name', 'model__model', 'color')
    list_filter = ('brand', 'model', 'type', 'status', 'year')
    ordering = ('-year', 'price')
    fieldsets = (
        (None, {
            'fields': ('owner', 'brand', 'model')
        }),
        ('Specifications', {
            'fields': ('price', 'color', 'type', 'status', 'year')
        }),
        ('Image', {
            'fields': ('image',)
        }),
    )