from django.shortcuts import render, redirect
from item.models import Category, Product
from .forms import SignupForm

def index(request):
    products = Product.objects.filter(is_sold=False)
    categories = Category.objects.all()
    return render(request, 'index.html', {
        'products': products,
        'categories': categories,
        })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {
        'form': form,
        })
