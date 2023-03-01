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

# import Order models
from .models import Order, OrderTrackItem, OrderFlpItem
from .serializers import OrderTrackSerializer, OrderFlpSerializer

# set User to custom user model
User = get_user_model()

# when user hits buy button in cart checkout, request comes here
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):

    print('\n Request.data obj: ' + '\n' + str(request.data) + '\n')
    '''
        REQUEST DATA LOOKS LIKE THIS:
        {
            'name': '97',
            'email': 'go78gligt',
            'phone': '7o8t78ot',
            'address1': '8o7t',
            'address2': 'y8l',
            'statePref': 'yl8oy',
            'country': 'lyi8yli8y',
            'zipcode': 'i8lyi',
            'items': [
                {
                    'flp_id': 4, 
                    'flp_name': 'Space Bossa', 
                    'flp_quantity': 0, 
                    'track_quantity': 0, 
                    'flp_price': '12.99'
                }
            ],
            'stripe_token': 'tok_1MgiFRIbgJsxEJrci3RQDzHW'
        }
    '''

    # bool to check if this is a US or Japan payment
    isUsd = True
    flp_paid_amount = 0
    track_paid_amount = 0
    total_usd_paid_amount = 0
    total_jpy_paid_amount = 0

    # check to see what kind of serializer to process:

    if 'flp' in str(request.data):
        serializer = OrderFlpSerializer(data=request.data)
    else:
        serializer = OrderTrackSerializer(data=request.data)



    if serializer.is_valid():

        print('\nprinting validated data\n')
        print(str(serializer.validated_data))
        # initialize stripe get stripe secret key from settings -> .env file
        stripe.api_key = settings.STRIPE_SK
        # check if this was jpy or usd purchase (usd is default)
        if isUsd:
            #
            total_usd_paid_amount = 1345
        # now do the same thing but for jpy
        else:
            # sum track/flp totals in total paid amount
            total_jpy_paid_amount = 12345
    

        # create the stripe Charge
        try:
            print('\n\nwe"re in the try block tryna create the Strpe charge\n\n')
            charge = stripe.Charge.create(
                # if it's usd, stripe takes amount in cents, otherwise leave it whole number for JPY
                amount = int(total_usd_paid_amount * 100) if isUsd is True else total_jpy_paid_amount,
                # usd or jpy
                currency='USD' if isUsd is True else 'JPY',
                description='Sherrif Crandy digital music/flp charge',
                # stripe token we get from frontend
                source=serializer.validated_data['stripe_token']
            )

            # calls OrderFlpSerializer or OrderTrackSerializer create function
            serializer.save(User=request.user, jpy_price=total_usd_paid_amount, usd_price=total_jpy_paid_amount)

            # pass this to frontend if everything was ok
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            print('something went wrong with serializer.save')
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