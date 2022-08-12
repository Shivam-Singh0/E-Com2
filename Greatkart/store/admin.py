from django.contrib import admin

from .models import Product

# Register your models here.
class Productad(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)} 

admin.site.register(Product, Productad)