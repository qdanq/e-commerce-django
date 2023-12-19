from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Product
from .forms import NewProductForm

def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    return render(request, 'detail.html', {
        'product': product,
        })


@login_required
def new(request):
    form = NewProductForm()

    return render(request, 'form.html', {
        'form': form
        })
