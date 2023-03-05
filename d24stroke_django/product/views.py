from django.db.models import Q
# from itertools import product
from django.http import Http404
import json

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name']
    def get_object (self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

class ProductsDetailView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'category': ["in", "exact"], 'description': ["in", "exact"], 'technical_details__brand': ["in", "exact"], 'technical_details__colour': ["in", "exact"], 'technical_details__tuning_level': ["in", "exact"], 'technical_details__material': ["in", "exact"], 'technical_details__cylinder_displacement': ["in", "exact"], 'technical_details__cylinder_piston_pin': ["in", "exact"], 'technical_details__cylinder_bore': ["in", "exact"], 'technical_details__cylinder_stroke': ["in", "exact"], 'technical_details__cylinder_conrod_length': ["in", "exact"], 'technical_details__bougie_thread': ["in", "exact"], 'technical_details__carburetor_type': ["in", "exact"], 'technical_details__carburetor_diameter': ["in", "exact"], 'technical_details__carburetor_airfilter_connection': ["in", "exact"], 'technical_details__carburetor_manifold_connection': ["in", "exact"], 'technical_details__carburetor_choke': ["in", "exact"], 'technical_details__carburetor_ports': ["in", "exact"], 'technical_details__variator_roller_size': ["in", "exact"], 'technical_details__variator_roller_weight': ["in", "exact"], 'technical_details__variator_range': ["in", "exact"], 'technical_details__clutch_diameter': ["in", "exact"], 'technical_details__transmission_type': ["in", "exact"], 'technical_details__ignition_lighting_supply': ["in", "exact"], 'technical_details__light_style': ["in", "exact"], 'technical_details__light_voltage': ["in", "exact"], 'technical_details__tire_width': ["in", "exact"], 'technical_details__tire_height': ["in", "exact"], 'technical_details__tire_rim_diameter': ["in", "exact"], 'technical_details__tire_code': ["in", "exact"], 'technical_details__tire_application': ["in", "exact"],
    'technical_details_dutch__merk': ["in", "exact"], 'technical_details_dutch__kleur': ["in", "exact"], 'technical_details_dutch__tuning_level': ["in", "exact"], 'technical_details_dutch__materiaal': ["in", "exact"], 'technical_details_dutch__cilinderinhoud': ["in", "exact"], 'technical_details_dutch__pistonpen': ["in", "exact"], 'technical_details_dutch__boring': ["in", "exact"], 'technical_details_dutch__krukas_slag': ["in", "exact"], 'technical_details_dutch__drijfstang_lengte': ["in", "exact"], 'technical_details_dutch__draad_bougie': ["in", "exact"], 'technical_details_dutch__type_carburateur': ["in", "exact"], 'technical_details_dutch__diameter_carburateur': ["in", "exact"], 'technical_details_dutch__luchtfilter_connectie': ["in", "exact"], 'technical_details_dutch__spruitstuk_connectie': ["in", "exact"], 'technical_details_dutch__choke_carburateur': ["in", "exact"], 'technical_details_dutch__poorten_carburateur': ["in", "exact"], 'technical_details_dutch__grootte_rollen_variateur': ["in", "exact"], 'technical_details_dutch__gewicht_rollen_variateur': ["in", "exact"], 'technical_details_dutch__lengte_variateur': ["in", "exact"], 'technical_details_dutch__diameter_koppeling': ["in", "exact"], 'technical_details_dutch__type_transmissie': ["in", "exact"], 'technical_details_dutch__lichtspoel_ontsteking': ["in", "exact"], 'technical_details_dutch__style_lamp': ["in", "exact"], 'technical_details_dutch__voltage_lamp': ["in", "exact"], 'technical_details_dutch__breedte_band': ["in", "exact"], 'technical_details_dutch__hoogte_band': ["in", "exact"], 'technical_details_dutch__velg_diameter_band': ["in", "exact"], 'technical_details_dutch__code_band': ["in", "exact"], 'technical_details_dutch__toepassing_band': ["in", "exact"]}
    search_fields = ['=name']
    ordering_fields = ['name', 'id']
    ordering = ['id']

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
        
