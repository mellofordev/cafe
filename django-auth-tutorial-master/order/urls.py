from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('purchase/', views.purchase, name='purchase'),
    path('cart/<slug:slug>',views.details,name='cart'),
]