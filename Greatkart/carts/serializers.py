from rest_framework import serializers

from carts.models import CartItems


class CartSerializer(serializers.ModelSerializer):
    created_by = serializers.CurrentUserDefault()

    class Meta:
        model = CartItems
        fields = [
            'product',
            'quantity',
            
        ]