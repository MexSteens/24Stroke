import stripe

from django.conf import settings
from django.http import Http404
from django.shortcuts import render

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order, OrderItem
from .serializers import OrderSerializer

@api_view(['POST'])
# @authentication_classes([authentication.TokenAuthentication])
# @permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        stripe.api_key = settings.STRIPE_SECRET_KEY
        paid_amount = sum(item.get('quantity') * item.get('product').price for item in serializer.validated_data['items'])

        try:
            charge = stripe.PaymentIntent.create(
                amount=int(paid_amount * 100),
                currency='EUR',
                description='Charge from 24stroke',
                payment_method_types=["card", "ideal", "bancontact", "sofort", "klarna"],
                # payment_method_data=serializer.validated_data['stripe_token']
            )
            if request.user.is_anonymous == False:
                serializer.save(user=request.user, paid_amount=paid_amount)
            else:
                serializer.save(paid_amount=paid_amount)

            print(charge.client_secret)
            return Response(charge.client_secret, status=status.HTTP_201_CREATED)
        except Exception:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    print(serializer.errors)
    
    return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

# class OrdersList(APIView):
#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request, format=None):
#         orders = Order.objects.filter(user=request.user)
#         serializer = MyOrderSerializer(orders, many=True)
#         return Response(serializer.data)
