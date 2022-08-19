from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from carts.serializers import CartSerializer
from carts.models import CartItems


class CartViewSet(viewsets.ModelViewSet):
    
    queryset = CartItems.objects.all()
    serializer_class = CartSerializer