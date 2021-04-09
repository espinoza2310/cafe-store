from django.shortcuts import render
from productapp.models import Product

# Create your views here.
def product(request):
    product=Product.objects.all()
    return render(request,"productapp/product.html",{'product': product})
