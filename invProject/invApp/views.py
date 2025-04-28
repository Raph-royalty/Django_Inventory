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
    if(request.method == 'POST'):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save();
            return redirect('product_list')
    return render(request, 'invApp/product_form.html', {'form': form})
#Read View
#Update View
#Delete View