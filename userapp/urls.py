"""
URL configuration for swiggyapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

app_name = 'userapp'
urlpatterns = [
    path('home/',views.home,name = 'home'),
    path('items/',views.items,name='items'),
    path('items/<str:product_name>/',views.each_item, name='each_item'),
    path('add/',views.add_item,name='add_item'),
    path('update/<str:product_name>/',views.update_item,name='update_item'),
    path('delete/<str:product_name>/',views.delete_item,name='delete_item')
]
