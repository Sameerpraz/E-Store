from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Product

class Cart(View):
    def get(self,request):
        # request.session.get('cart') le chai yo {'1': 1, '2': 1, '5': 2} formate ma value print garxa
        # request.session.get('cart').keys() le chai (['1', '2', '5'])
        ids =list(request.session.get('cart').keys())
        products = Product.get_into_cart(ids)
        print(products)
        return render(request, 'cart.html',{
            'products': products
        })