from django.contrib import admin

# Register your models here.
from .models import Category, Product, CartItem

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Product, ProductAdmin)
admin.site.register(CartItem)