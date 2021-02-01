from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('category/<int:pk>/',views.CategoryView,name='category')
]