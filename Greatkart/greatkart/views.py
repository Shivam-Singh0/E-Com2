

from django.shortcuts import render
from django.db.models import Q
from store.models import Product

def  home(request):
    products = Product.objects.all()
    item_name = request.GET.get('item_name')
    if item_name:
        products = Product.objects.filter(product_name__icontains=item_name)
        pro_count = products.count()
        return render(request, 'store/store.html', {'products':products, 'pro_count':pro_count})
    
    return render(request, 'home.html', {'products':products})


