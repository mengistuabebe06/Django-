from django.shortcuts import render, get_object_or_404
from store.models import Product
from category.models import Category

# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None
   # this is used to display a product using categories 
   # first register the url and pass to view.store  path('<slug:category_slug>/',views.store, name="products_by_category"),
   # then do the below code 
   #
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available= True)
        product_count = products.count()
    else:
        
        #do query for feathing all data from product from table 
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)


