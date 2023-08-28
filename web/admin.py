from django.contrib import admin
from .models import Category, Product,Product_images
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)



class Product_imagesInline(admin.TabularInline):
    model = Product_images

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [Product_imagesInline]

admin.site.register(Product, ProductAdmin)