from django.shortcuts import render, redirect

# Create your views here.
from .forms import ProductForm
from .models import Product

#Home View

def home_view(request):
    return render(request, 'invApp/home.html')

#Create View
def create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save();
            return redirect('product_list')
    return render(request, 'invApp/product_form.html', {'form': form})
#Read View
def product_view(request):
    products = Product.objects.all()
    return render(request, 'invApp/product_list.html', {'products': products})
#Update View
def product_update(request, product_id):
    product = Product.objects.get(product_id=product_id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance = product)

        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'invApp/product_form.html', {'form': form})

#Delete View
def product_delete(request, product_id):
    product = Product.objects.get(product_id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'invApp/confirm_delete.html', {'product': product})

    




