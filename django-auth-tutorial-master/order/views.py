from django.shortcuts import render
from .models import Purchase
from math import ceil
def purchase(request):
    products=Purchase.objects.all()
    length=len(products)


    list = {'product':products}
    print(list)
    return render(request,'purchase.html',list)
def details(request,slug):
    product = Purchase.objects.get(slug=slug)
    return  render(request,'cart.html',{'product':product})