from django.urls import path, include
from .import views
from rest_framework import routers
from .viewsets import CartViewSet


router = routers.DefaultRouter()
router.register(r'api', CartViewSet)
urlpatterns = [
    path('', views.cart, name="cart"),
    path('', include(router.urls)),
    path('add_cart/<int:product_id>', views.add_cart, name="add_cart"),
    path('dec_quan/<int:product_id>', views.dec_quan, name="dec_quan"),
    path('remove_cart/<int:product_id>', views.remove_cart, name="remove_cart"),
    
] 
