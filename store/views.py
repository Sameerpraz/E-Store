from django.db.models import Count
from django.shortcuts import render
from .models.product import Product
from .models.category import Category
from django.http import HttpResponse


# Create your views here.

def index(request):
    total = []
    products = Product.get_all_products()
    categories = Category.objects.all()

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



def CategoryView(request,pk):
    category_blogs = Product.objects.filter(category_id=pk)
    category_name=Category.objects.filter(pk=pk)

    return render(request, 'store/category.html',{
        'cats': category_name,
        'category_blogs': category_blogs
        })
