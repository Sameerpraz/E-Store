from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category_id', 'image']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname','email', 'phone','password']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Customer,CustomerAdmin)
