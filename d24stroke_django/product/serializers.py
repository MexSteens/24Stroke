from rest_framework import serializers

from .models import Category, Product, Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            "name",
            "get_image",
            "default"
        )

class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            # "get_image",
            "images",
            "get_thumbnail"
        )

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
        )

# class SubCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SubCategory
#         fields = (
#             "id",
#             "name",
#             "get_absolute_url",
#             "products",
#         )


    

