from .models import CartItems
from carts.views import _cart_id

def cart_length(request):
    cart_len = CartItems.objects.filter(cart__cart_id = _cart_id(request))
    return dict(cart_links=cart_len)