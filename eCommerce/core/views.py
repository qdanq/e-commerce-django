from django.shortcuts import render

from item.models import Category, Product

def index(request):
    products = Product.objects.filter(is_sold=False)
    return render(request, 'index.html')
