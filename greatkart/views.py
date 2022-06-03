from django.shortcuts import render
from store.models import Product

def home(request):
    #do query for feathing all data from product from table 
    products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products,
    }
    return render(request, "home.html", context)