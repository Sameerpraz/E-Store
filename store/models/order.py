from django.db import models
from .category import Category
from .product import Product
from .customer import Customer
import datetime


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    date = models.DateField(default=datetime.datetime.today)
