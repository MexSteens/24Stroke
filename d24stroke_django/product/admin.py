from ast import Sub
from unicodedata import category
from django.contrib import admin

from .models import Category, Product, Subscriber, Image

# Register your models here.
# admin.site.register(Category)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Subscriber)
admin.site.register(Image)