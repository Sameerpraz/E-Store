from django.db.models import Count
from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib import auth

# from store.models.customer import Customer
from django.views import View
from django.contrib.auth import authenticate
# password hashing
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password


class Index(View):
    def post(self,request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart={}
            cart[product] = 1
        request.session['cart']=cart
        print('--------------------------------')
        print(request.session['cart'])
        return redirect('index')
    def get(self,request):
        # print('------')
        # print(request.session.get('firstname'))
        cart= request.session.get('cart')
        if not cart:
            request.session['cart']={}
        total = []
        products = None
        categories = Category.objects.all()
        categoryID = request.GET.get('category')
        
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()


        for category in categories:
            cat_id = category.id
            value = Product.objects.filter(category=cat_id).count()
            total.append(value)
        # we can use zip only when size of list is same
        data = zip(categories, total)
        return render(request, 'store/index.html', {
            'products': products,
            'data': data
            })

    


# def index(request):
    