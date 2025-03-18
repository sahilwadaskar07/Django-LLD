from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    return render(request, 'electronics/home.html')

def about(request):
    return render(request , 'electronics/about.html')

def product_detail(request):
    return render(request, 'electronics/product_detail.html')

def product_detail(request):
    prod = Product.objects.all()
    return render(request , 'electronics/product_detail.html', {"prod": prod})

