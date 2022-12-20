from rest_framework import serializers

from .models import Category, Product, Image, TechnicalDetails

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            "name",
            "get_image",
            "default"
        )

class TechnicalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalDetails
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    technical_details = TechnicalDetailsSerializer()
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "price",
            "technical_details",
            "images",
            "get_absolute_url",
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


    

