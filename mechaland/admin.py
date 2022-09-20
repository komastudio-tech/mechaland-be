from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductSpecs)
admin.site.register(ProductVariant)
admin.site.register(ProductImage)
admin.site.register(HeroImage)
admin.site.register(FeaturedCollection)
admin.site.register(InterestCheck)