from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import User
from .forms import ProductForm
from django import forms
# Create your views here.

def home(request):
    return render(request,'userapp/base.html')


def items(request):
    user = User.objects.all()
    context = {'user':user}
    return render(request,'userapp/items.html',context)

def each_item(request,product_name):
    item = get_object_or_404(User,product_name=product_name)
    context = {'item':item}
    return render(request,'userapp/detail.html',context)

def add_item(request):
    newitem = ProductForm(request.POST or None)
    if newitem.is_valid():
        newitem.save()
        return redirect('userapp:items')
    return render(request,'userapp/newitem.html',{'newitem':newitem})

def update_item(request,product_name):
    pro = get_object_or_404(User,product_name=product_name)
    form = ProductForm(instance=pro)
    if request.method == "POST":
        form = ProductForm(request.POST,instance=pro)
        if form.is_valid():
            form.save()
            return redirect('userapp:items')
    return render(request,'userapp/update.html',{'form':form})    

def delete_item(request,product_name):
    item = get_object_or_404(User,product_name=product_name)
    if request.method == 'POST':
        item.delete()
        return redirect('userapp:items')
    return render(request,'userapp/delete.html',{'item':item})    
