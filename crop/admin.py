from django.contrib import admin

from .models import User, Seller, Buyer, Crop, CropDetail, Order

# Register your models here.

admin.site.register(User)
admin.site.register(Seller)
admin.site.register(Buyer)
admin.site.register(Crop)
admin.site.register(CropDetail)
admin.site.register(Order)