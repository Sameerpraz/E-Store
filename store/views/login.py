from django.db.models import Count
from django.shortcuts import render, redirect
# from .models.product import Product
# from .models.category import Category
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib import auth

from store.models.customer import Customer
from django.views import View
from django.contrib.auth import authenticate
# password hashing
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        error_message = None
        email =request.POST.get('email')
        password =  request.POST.get('password')
        # customer = Customer.objects.get(email=email)
        # customer = Customer.get_customer_by_email(email)
        try:
            customer = Customer.objects.get(email=email)
            value = {
                'email' : email 
                }
        except Customer.DoesNotExist:
            customer = None
            value = {
                'email' : email 
                }

        

        if customer:
            passwordmatch = check_password(password, customer.password)

            if passwordmatch:
                # we are passing object customer for login 
                request.session['customer'] = customer.id
                return redirect('index')
            else:
                error_message = "Password doesn't match"
                return render(request,'login.html',{
                    'error' : error_message,
                    'values': value
                    })
        else:
            error_message = "User doesnot exit"
            return render(request,'login.html',{
                'error' : error_message,
                'values': value
            })



def logout(request):
    request.session.clear()
    return redirect('index')