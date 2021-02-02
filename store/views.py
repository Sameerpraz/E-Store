from django.db.models import Count
from django.shortcuts import render, redirect
from .models.product import Product
from .models.category import Category
from django.http import HttpResponse


from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View

# Create your views here.

def index(request):
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


def login(request):
    return render(request,'login.html')




def Register(request):  
    
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        PostData = request.POST
        first_name = PostData.get('firstname')
        last_name = PostData.get('lastname')
        email = PostData.get('email')
        phone = PostData.get('phone')
        password = PostData.get('password')
        confirm_password = PostData.get('confirm_password')
    

    values ={
        'first_name' : first_name,
        'last_name' : last_name ,
        'phone' : phone,            
        'email' : email
    }

    # validation (checking of error )
    # used_email = 
    error_message = None
    if(not first_name):
        error_message = "First name is Required."
    elif len(first_name)<4:
        error_message = "Length must be if 4 letters."
    # elif len(phone)<6:
    #     error_message = "Phone number must be of 10 digits."
    elif(password !=confirm_password):
        error_message = "Password must be same."
    
    # Checking unique email 
    elif(password ==confirm_password):
        if Customer.objects.filter(email=email):
            error_message='The email you entered has already been taken. Please try another email.'

    

    #success (saving)
    if (not error_message):
        customer = Customer(
            firstname = first_name,
            lastname = last_name ,
            email = email,
            phone = phone,
            password = password
        )
        customer.register()
        return render(request, 'login.html')
    else:
        return render(request, 'register.html',{
            'error': error_message,
            'value': values
        })
        

