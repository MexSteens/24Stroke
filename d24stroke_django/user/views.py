from django.shortcuts import render
from .models import BillingAddress, UserAddress
from .serializers import BillingAddressSerializer, UserAddressSerializer
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework import status


from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class BillingAddressDetail(APIView):
    def get_object(self, user_id):
        try:
            return BillingAddress.objects.get(user=user_id)
        except BillingAddress.DoesNotExist:
            raise Http404

    def get(self, request, user_id, format=None):
        billing_address = self.get_object(user_id)
        serializer = BillingAddressSerializer(billing_address)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        billing_address = self.get_object(pk)
        serializer = BillingAddressSerializer(billing_address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BillingAddressList(APIView):
    def post(self, request, format=None):
        serializer = BillingAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserAddressDetail(APIView):
    def get_object(self, user_id):
        try:
            return UserAddress.objects.get(user=user_id)
        except UserAddress.DoesNotExist:
            raise Http404

    def get(self, request, user_id, format=None):
        User_address = self.get_object(user_id)
        serializer = UserAddressSerializer(User_address)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        User_address = self.get_object(pk)
        serializer = UserAddressSerializer(User_address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserAddressList(APIView):
    def post(self, request, format=None):
        serializer = UserAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)