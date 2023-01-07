from django.db.models import Q
# from itertools import product
from django.http import Http404
import json


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product, Category, Subscriber, Image, HighlightedProduct
from .serializers import CategorySerializer, ProductSerializer, ImageSerializer, HighlightedProductSerializer

# Create your views here.
class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ImageDetail(APIView):
    def get_object(self, product_slug, image_slug):
        try:
            return Image.objects.filter(product__slug=product_slug).get(slug=image_slug)
        except Image.DoesNotExist:
            raise Http404

    def get(self, request, product_slug, image_slug, format=None):
        image = self.get_object(product_slug, image_slug)
        serializer = ImageSerializer(image)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get_object (self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

class HighlightedProductDetail(APIView):
    # def get_object (self):
    #     try:
    #         return HighlightedProduct.objects.get()
    #     except HighlightedProduct.DoesNotExist:
    #         raise "errorororor"
    
    def get(self, request, format=None):
        highlighted_product = HighlightedProduct.objects.all()[0:4]
        serializer = HighlightedProductSerializer(highlighted_product, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})

@api_view(['POST'])
def api_add_subscriber(request):
    email = request.data['email']

    s=Subscriber.objects.create(email=email)
    
    return Response({'success': True})
        
