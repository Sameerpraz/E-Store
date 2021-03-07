from django.db import models


class Customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname
    


    def register(self):
        self.save()
    

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
    