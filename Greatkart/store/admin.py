
from django.contrib import admin

from .models import Product, Variations

# Register your models here.
class Productad(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}

class VariationAd(admin.ModelAdmin):
    list_display = ('product','variations_category',
    'variation_value',
    'is_active',
    'created_date',
)

admin.site.register(Product, Productad)
admin.site.register(Variations, VariationAd)