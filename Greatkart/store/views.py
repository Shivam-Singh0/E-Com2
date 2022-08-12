from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
# Create your views here.
def store(request, cat_slug=None):
    if cat_slug:
        category =  get_object_or_404(Category, slug=cat_slug)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    pro_count = products.count()
    return render(request, 'store/store.html', {'products':products, 'pro_count':pro_count})



def detail(request,product_slug,cat_slug):
    cat_slug = None
    ind_products = get_object_or_404(Product, slug=product_slug)
    return render(request, 'store/detail.html', {'ind_products':ind_products})