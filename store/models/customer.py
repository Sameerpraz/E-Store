from django.db import models


class Customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(unique=True)
    password = models.CharField(max_length=50)



    def register(self):
        self.save()
    