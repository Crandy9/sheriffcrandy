# to talk to Stripe API
import stripe
from django.conf import settings
# get custom users
from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import render

# drf imports
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response


# set User to user model
User = get_user_model()

# import Order models
from .models import Order, OrderItem
from .serializers import OrderSerializer

# when user hits buy button in cart checkout modal, request comes here
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):

    # bool to check if this is a US or Japan payment
    isUsd = True

    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        # get stripe secret key from settings -> .env file
        stripe.api_key = settings.STRIPE_SK
        # check if this was jpy or usd purchase (usd is default)
        if isUsd:
            # get flp total if any 
            if (serializer.validated_data['items'].get('flp_quantity') == 0):
                flp_paid_amount = 0
            else :
                flp_paid_amount = sum(item.get('flp').usd_flp_price for item in serializer.validated_data['items'])
            
            # get track total if any 
            if (serializer.validated_data['items'].get('track_quantity') == 0):
                track_paid_amount = 0
            else:
                track_paid_amount = sum(item.get('track').usd_track_price for item in serializer.validated_data['items'])
            
            # sum track/flp totals in total paid amount
            total_paid_amount = flp_paid_amount + track_paid_amount
        # now do the same thing but for jpy
        else:
            # get flp total if any 
            if (serializer.validated_data['items'].get('flp_quantity') == 0):
                flp_paid_amount = 0
            else :
                flp_paid_amount = sum(item.get('flp').jpy_flp_price for item in serializer.validated_data['items'])
            
            # get track total if any 
            if (serializer.validated_data['items'].get('track_quantity') == 0):
                track_paid_amount = 0
            else:
                track_paid_amount = sum(item.get('track').jpy_track_price for item in serializer.validated_data['items'])
            
            # sum track/flp totals in total paid amount
            total_paid_amount = flp_paid_amount + track_paid_amount
    

        # create the stripe Charge
        try:
            charge = stripe.Charge.create(
                # if it's usd, stripe takes amount in cents, otherwise leave it whole number for JPY
                amount = int(total_paid_amount * 100) if isUsd is True else total_paid_amount,
                # usd or jpy
                currency='USD' if isUsd is True else 'JPY',
                description='Sherrif Crandy digital music/flp charge',
                # stripe token we get from frontend
                source=serializer.validated_data['stripe_token']
            )

            serializer.save(User=request.user, paid_amount=total_paid_amount)

            # pass this to frontend if everything was ok
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            print('something went wrong with charge or serializer.save')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # if something is wrong with serializer
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrdersList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)