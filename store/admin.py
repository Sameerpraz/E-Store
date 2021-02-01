from django.contrib import admin
from .models.product import Product
from .models.category import Category
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category_id', 'image']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
