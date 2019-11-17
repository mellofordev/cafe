from django.shortcuts import render
from .models import Menu
# Create your views here.
def menu(request):


    menu = Menu.objects.all()
    list ={'menu':menu}





    return render(request,'menu.html',list)