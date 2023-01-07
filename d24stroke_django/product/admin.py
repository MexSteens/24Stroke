from ast import Sub
from unicodedata import category
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Category, Product, Subscriber, Image, TechnicalDetails, HighlightedProduct, User

class ProductImagesInline(admin.TabularInline):
    model = Image

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImagesInline]

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Subscriber)
admin.site.register(TechnicalDetails)
admin.site.register(HighlightedProduct)
