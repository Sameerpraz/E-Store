from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    price = models.FloatField()
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/')


    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()
        