from django.contrib import admin
from .models import Category, Product, SubCategory, UserProfile, Brand, Purchase

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(SubCategory)
admin.site.register(UserProfile)
admin.site.register(Brand)
admin.site.register(Purchase)