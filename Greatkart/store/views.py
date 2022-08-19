
from django.shortcuts import render, get_object_or_404

from carts.models import CartItems
from .models import Product
from category.models import Category
from carts.views import _cart_id
from django.core.paginator import Paginator
from django.http import HttpResponse
# Create your views here.
def store(request, cat_slug=None):
    item_name = request.GET.get('item_name')
    if cat_slug:
        category =  get_object_or_404(Category, slug=cat_slug)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all().order_by('id')

    
    if item_name:
        products = Product.objects.filter(product_name__icontains=item_name)
        
    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)
    pro_count = products.count()
    return render(request, 'store/store.html', { 'pro_count':pro_count, 'products':paged_product})



def detail(request,product_slug,cat_slug):
    
    
    ind_products = get_object_or_404(Product, slug=product_slug, category__slug=cat_slug)
    in_cart = CartItems.objects.filter(cart__cart_id=_cart_id(request), product=ind_products).exists()
    return render(request, 'store/detail.html', {'ind_products':ind_products, 'in_cart':in_cart})