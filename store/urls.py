from django.urls import path, include

from .views.home import Index
from .views.login import *
from .views.register import *

urlpatterns = [
    path('',Index.as_view(),name='index'),
    # path('category/<int:pk>/',views.CategoryView,name='category')
    path('register', Register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    
]