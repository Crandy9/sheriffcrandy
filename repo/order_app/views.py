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
from .models import Order, OrderFlpItem #, OrderTrackItem 
from .serializers import OrderFlpSerializer, OrderTrackSerializer

# import track and flp models
from flps_app.models import *
from tracks_app.models import *



# when user hits buy button in cart checkout, request comes here
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):


    # bool to check if this is a US or Japan payment
    isUsd = True

    # TRACKS ONLY - paid only, free only, paid and free
    if 'no_flps' in str(request.data):
        print('WHAT THE HEEEEEEEE TRACKS ONLY')
        serializer = OrderTrackSerializer(data=request.data)
        
        if serializer.is_valid():

            usd_paid_amount = 0
            jpy_paid_amount = 0
            # check if this was jpy or usd purchase (usd is default)
            if isUsd:
                for item in serializer.validated_data['track_items']:
                    if item.get('track').is_free:
                        print('\ntrack ' + str(item.get('track').title) + ' is a free track\n')
                        pass
                    else: 
                        usd_paid_amount += item.get('track').usd_price
            # now do the same thing but for jpy
            else:
                for item in serializer.validated_data['track_items']:
                    if item.get('track').is_free:
                        print('\ntrack ' + str(item.get('track').title) + ' is a free track\n')
                        pass
                    else: 
                        jpy_paid_amount += item.get('track').jpy_price
        
            amountStripeWillCharge = int(usd_paid_amount * 100) if isUsd is True else jpy_paid_amount
            
            # if it's 0, that means user downloaded free stuff, don't create a stripe charge, just save download history to DB
            if usd_paid_amount == 0:
                print('User downloading free tracks only')
                serializer.save(user=request.user, usd_paid_amount=usd_paid_amount, jpy_paid_amount=jpy_paid_amount)
                for item in serializer.validated_data['track_items']:
                    my_track = Track.objects.get(title=item.get('track').title)
                    my_track.purchase_count += 1
                    my_track.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                try:
                    stripe.api_key = settings.STRIPE_SK
                    charge = stripe.Charge.create(
                        # if it's usd, stripe takes amount in cents, otherwise leave it whole number for JPY
                        amount = amountStripeWillCharge,
                        # usd or jpy
                        currency='USD' if isUsd is True else 'JPY',
                        description='Sherrif Crandy digital audio track download charge',
                        # stripe token we get from frontend
                        source=serializer.validated_data['stripe_token']
                    )

                    # saving OrderFlpSerializer or OrderTrackSerializer create function
                    serializer.save(user=request.user, usd_paid_amount=usd_paid_amount, jpy_paid_amount=jpy_paid_amount)

                    for item in serializer.validated_data['track_items']:
                        my_track = Track.objects.get(title=item.get('track').title)
                        my_track.purchase_count += 1
                        my_track.save()

                    # pass this to frontend if everything was ok
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                except Exception:
                    print('something went wrong with track serializer.save')
                    print('here are the track errors')
                    print(str(serializer.errors))
                    print(serializer.errors)
                    print('here is the track serializer')
                    print('\n' + str(serializer) + '\n')
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # if something is wrong with serializer
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    # FLPS ONLY - paid only, free only, paid and free
    elif 'no_tracks' in str(request.data):
        print('WHAT THE HEEEEEEEE FLPS ONLY')
        serializer = OrderFlpSerializer(data=request.data)


        if serializer.is_valid():

            usd_paid_amount = 0
            jpy_paid_amount = 0
            # check if this was jpy or usd purchase (usd is default)
            if isUsd:
                for item in serializer.validated_data['flp_items']:
                    if item.get('flp').flp_is_free:
                        print('\flp ' + str(item.get('flp').flp_name) + ' is a free download\n')
                        pass
                    else: 
                        usd_paid_amount += item.get('flp').usd_price
            else:
                for item in serializer.validated_data['flp_items']:
                    if item.get('flp').flp_is_free:
                        print('\flp ' + str(item.get('flp').flp_name) + ' is a free download\n')
                        pass
                    else: 
                        jpy_paid_amount += item.get('flp').jpy_price
        
            amountStripeWillCharge = int(usd_paid_amount * 100) if isUsd is True else jpy_paid_amount

            # if it's 0, that means user downloaded free stuff, don't create a stripe charge, just save download history to DB
            if usd_paid_amount == 0:
                print('User downloading free flps only')
                serializer.save(user=request.user, usd_paid_amount=usd_paid_amount, jpy_paid_amount=jpy_paid_amount)
                for item in serializer.validated_data['flp_items']:
                    my_flp = Flp.objects.get(flp_name=item.get('flp').flp_name)
                    my_flp.purchase_count += 1
                    my_flp.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                try:
                    stripe.api_key = settings.STRIPE_SK
                    charge = stripe.Charge.create(
                        # if it's usd, stripe takes amount in cents, otherwise leave it whole number for JPY
                        amount = amountStripeWillCharge,
                        # usd or jpy
                        currency='USD' if isUsd is True else 'JPY',
                        description='Sherrif Crandy FLP zip file download charge',
                        # stripe token we get from frontend
                        source=serializer.validated_data['stripe_token']
                    )

                    # saving OrderFlpSerializer or OrderTrackSerializer create function
                    serializer.save(user=request.user, usd_paid_amount=usd_paid_amount, jpy_paid_amount=jpy_paid_amount)
                    for item in serializer.validated_data['flp_items']:
                        my_flp = Flp.objects.get(flp_name=item.get('flp').flp_name)
                        my_flp.purchase_count += 1
                        my_flp.save()
                    # pass this to frontend if everything was ok
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                except Exception:
                    print('something went wrong with flp serializer.save')
                    print('here are the flp errors')
                    print(str(serializer.errors))
                    print(serializer.errors)
                    print('here is the flp serializer')
                    print('\n' + str(serializer) + '\n')
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # if something is wrong with serializer
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # TRACKS AND FLPS 
    # TODO
    else:
        print('WHAT THE HEEEEEEEE TRACKS AND FLPS')
        # need to import copy to create two seperate instances of the request.data object.
        # dumb python design
        import copy
        flp_amountStripeWillCharge = 0
        track_amountStripeWillCharge = 0

        '''
        gameplan:

            since request.data is a dictionary containing both track and flp data,
            we have to create two separate dictionaries and process them separately
            so for flps, we have to pop off 'track_items' and then we can process it normally
            for tracks, we have to pop off 'flp_items' and then we can process it normally
        '''

        flp_dict = request.data
        track_dict = copy.deepcopy(flp_dict)


        flp_dict.pop('track_items') 
        track_dict.pop('flp_items') 


        # process track_dict
        track_dict_serializer = OrderTrackSerializer(data=track_dict)
        
        if track_dict_serializer.is_valid():

            usd_paid_amount = 0
            jpy_paid_amount = 0
            # check if this was jpy or usd purchase (usd is default)
            if isUsd:
                for item in track_dict_serializer.validated_data['track_items']:
                    if item.get('track').is_free:
                        print('\ntrack ' + str(item.get('track').title) + ' is a free track\n')
                        pass
                    else: 
                        usd_paid_amount += item.get('track').usd_price
            # now do the same thing but for jpy
            else:
                for item in track_dict_serializer.validated_data['track_items']:
                    if item.get('track').is_free:
                        print('\ntrack ' + str(item.get('track').title) + ' is a free track\n')
                        pass
                    else: 
                        jpy_paid_amount += item.get('track').jpy_price
        
            track_amountStripeWillCharge = int(usd_paid_amount * 100) if isUsd is True else jpy_paid_amount
            
            # if it's 0, that means user downloaded free stuff, don't create a stripe charge, just save download history to DB
            if usd_paid_amount == 0:
                print('User downloading free tracks only')
                track_dict_serializer.save(user=request.user, usd_paid_amount=usd_paid_amount, jpy_paid_amount=jpy_paid_amount)
                for item in track_dict_serializer.validated_data['track_items']:
                    my_track = Track.objects.get(title=item.get('track').title)
                    my_track.purchase_count += 1
                    my_track.save()
            else:
                try:
                    # saving OrderFlpSerializer or OrderTrackSerializer create function
                    track_dict_serializer.save(user=request.user, usd_paid_amount=usd_paid_amount, jpy_paid_amount=jpy_paid_amount)

                    for item in track_dict_serializer.validated_data['track_items']:
                        my_track = Track.objects.get(title=item.get('track').title)
                        my_track.purchase_count += 1
                        my_track.save()

                except Exception:
                    print('something went wrong with track serializer.save')
                    print('here are the track errors')
                    print(str(track_dict_serializer.errors))
                    print(track_dict_serializer.errors)
                    print('here is the track track_dict_serializer')
                    print('\n' + str(track_dict_serializer) + '\n')
    

        print('\ntrack data processed\n')

        # process flp_dict
        flp_dict_serializer = OrderFlpSerializer(data=flp_dict)
        
        if flp_dict_serializer.is_valid():

            usd_paid_amount = 0
            jpy_paid_amount = 0
            # check if this was jpy or usd purchase (usd is default)
            if isUsd:
                for item in flp_dict_serializer.validated_data['flp_items']:
                    if item.get('flp').flp_is_free:
                        print('\flp ' + str(item.get('flp').flp_name) + ' is a free flp\n')
                        pass
                    else: 
                        usd_paid_amount += item.get('flp').usd_price
            # now do the same thing but for jpy
            else:
                for item in flp_dict_serializer.validated_data['flp_items']:
                    if item.get('flp').flp_is_free:
                        print('\flp ' + str(item.get('flp').flp_name) + ' is a free flp\n')
                        pass
                    else: 
                        jpy_paid_amount += item.get('flp').jpy_price
        
            flp_amountStripeWillCharge = int(usd_paid_amount * 100) if isUsd is True else jpy_paid_amount
            
            # if it's 0, that means user downloaded free stuff, don't create a stripe charge, just save download history to DB
            if usd_paid_amount == 0:
                print('User downloading free flps only')
                flp_dict_serializer.save(user=request.user, usd_paid_amount=usd_paid_amount, jpy_paid_amount=jpy_paid_amount)
                for item in flp_dict_serializer.validated_data['flp_items']:
                    my_flp = Flp.objects.get(flp_name=item.get('flp').flp_name)
                    my_flp.purchase_count += 1
                    my_flp.save()
                # returning both serializer datas
                print('\nflp data processed\n')
                return Response(status=status.HTTP_201_CREATED)
            else:
                try:
                    stripe.api_key = settings.STRIPE_SK
                    charge = stripe.Charge.create(
                        # if it's usd, stripe takes amount in cents, otherwise leave it whole number for JPY
                        amount = flp_amountStripeWillCharge + track_amountStripeWillCharge,
                        # usd or jpy
                        currency='USD' if isUsd is True else 'JPY',
                        description='Sherrif Crandy digital flp/audio file download charge',
                        # stripe token we get from frontend
                        source=flp_dict_serializer.validated_data['stripe_token']
                    )

                    # saving OrderFlpSerializer or OrderTrackSerializer create function
                    flp_dict_serializer.save(user=request.user, usd_paid_amount=usd_paid_amount, jpy_paid_amount=jpy_paid_amount)

                    for item in flp_dict_serializer.validated_data['flp_items']:
                        my_flp = Flp.objects.get(flp_name=item.get('flp').flp_name)
                        my_flp.purchase_count += 1
                        my_flp.save()

                    # pass this to frontend if everything was ok
                    print('\nflp data processed\n')
                    return Response(status=status.HTTP_201_CREATED)
                except Exception:
                    print('something went wrong with flp_dict_serializer.save')
                    print('here are the track errors')
                    print(str(flp_dict_serializer.errors))
                    print(flp_dict_serializer.errors)
                    print('here is the track track_dict_serializer')
                    print('\n' + str(flp_dict_serializer) + '\n')
                    return Response(status=status.HTTP_400_BAD_REQUEST)
        
        # if something is wrong with flp_dict_serializer
        return Response(status=status.HTTP_400_BAD_REQUEST)










'''
class OrdersList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)
'''