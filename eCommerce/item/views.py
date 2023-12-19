from django.shortcuts import render, get_object_or_404, redirect
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
    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()

            return redirect('item:detail', pk=product.id)
    else:
        form = NewProductForm()


    return render(request, 'form.html', {
        'form': form
        })
