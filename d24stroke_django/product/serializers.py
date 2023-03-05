from rest_framework import serializers

from .models import Category, Product, Image, TechnicalDetails, HighlightedProduct, TechnicalDetailsDutch
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

# class UserRegistrationSerializer(BaseUserRegistrationSerializer):
#     class Meta(BaseUserRegistrationSerializer.Meta):
#         model = User
#         fields = '__all__'

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

class TechnicalDetailsSerializerDutch(serializers.ModelSerializer):
    class Meta:
        model = TechnicalDetailsDutch
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    technical_details = TechnicalDetailsSerializer()
    technical_details_dutch = TechnicalDetailsSerializerDutch()

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "price",
            "technical_details",
            "technical_details_dutch",
            "images",
            "get_absolute_url",
            "get_thumbnail",
            "category"
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

class HighlightedProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = HighlightedProduct
        fields = '__all__'

# class SubCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SubCategory
#         fields = (
#             "id",
#             "name",
#             "get_absolute_url",
#             "products",
#         )


    

