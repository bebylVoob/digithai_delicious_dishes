from django.contrib import admin

from cuisine.models import Cuisine, Dishes


# ContentProviderShare
class InlineDishes(admin.TabularInline):
    model = Dishes
    fields = ('name', 'desc', 'image')
    verbose_name = 'name'
    extra = 1


@admin.register(Cuisine)
class CuisineAdmin(admin.ModelAdmin):
    inlines = [InlineDishes]
    list_display = (
        'id',
        'type_name',
        'datetime_create',
        'datetime_update'
    )
    search_fields = ('type_name',)


@admin.register(Dishes)
class DishesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'desc',
        'image',
        'datetime_create',
        'datetime_update'
    )
    search_fields = ('name',)
