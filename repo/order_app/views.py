# to talk to Stripe API
import stripe
from django.conf import settings
# get custom users

# drf imports
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

# import Order serializers
from .serializers import OrderFlpSerializer, OrderTrackSerializer
# import flps+app and tracks_app serializers
from flps_app.serializers import FlpSerializer
from tracks_app.serializers import TrackSerializer

# import track and flp models
from flps_app.models import *
from tracks_app.models import *


# media path to return tracks/flps
path = os.path.join(settings.MEDIA_ROOT, '')
def downloads(request):
    pass



    

# when user hits buy button in cart checkout, request comes here
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):

    print('\n\n Raw Request post data:\n' + str(request.data) + '\n\n')
    # bool to check if this is a US or Japan payment
    isUsd = True
    # need to import copy to create two seperate instances of the request.data object.
    # dumb python design
    import copy
    flp_amountStripeWillCharge = 0
    track_amountStripeWillCharge = 0

    flp_dict = request.data
    track_dict = copy.deepcopy(flp_dict)

    # remove irrelevant data from both dicts
    flp_dict.pop('track_items') 
    track_dict.pop('flp_items') 
    print('\n\n FLP DICT:\n' + str(flp_dict) + '\n\n')
    print('\n\n TRACK DICT:\n' + str(track_dict) + '\n\n')

    
    # don't attempt to create serializer for tracks if none exists
    if 'no_tracks' in str(track_dict):
        print('\n\nNo tracks to process\n\n')
        pass
    else:
        print('\n\nProcessing Tracks\n\n')
        # process track_dict
        track_dict_serializer = OrderTrackSerializer(data=track_dict)
        
        if track_dict_serializer.is_valid():

            track_usd_paid_amount = 0
            track_jpy_paid_amount = 0
            # check if this was jpy or usd purchase (usd is default)
            if isUsd:
                for item in track_dict_serializer.validated_data['track_items']:
                    if item.get('track').is_free:
                        print('\ntrack ' + str(item.get('track').title) + ' is a free track\n')
                        pass
                    else: 
                        track_usd_paid_amount += item.get('track').usd_price
            # for jpy
            else:
                for item in track_dict_serializer.validated_data['track_items']:
                    if item.get('track').is_free:
                        print('\ntrack ' + str(item.get('track').title) + ' is a free track\n')
                        pass
                    else: 
                        track_jpy_paid_amount += item.get('track').jpy_price
        
            track_amountStripeWillCharge = int(track_usd_paid_amount * 100) if isUsd is True else track_jpy_paid_amount
            
            # if there are flps to process, don't create stripe charge or return any data yet
            try:
                if not 'no_flps' in str(flp_dict):
                    print('\n flps need to be processed as well \n')
                    pass
                # else if there are only tracks to process, create the Stripe charge and save the serializer
                else:
                    print('\nthere are no flps to process \n')
                    stripe.api_key = settings.STRIPE_SK
                    charge = stripe.Charge.create(
                        # if it's usd, stripe takes amount in cents, otherwise leave it whole number for JPY
                        amount = track_amountStripeWillCharge,
                        # usd or jpy
                        currency='USD' if isUsd is True else 'JPY',
                        description='Sherrif Crandy digital audio track download charge',
                        # stripe token we get from frontend
                        source=track_dict_serializer.validated_data['stripe_token']
                    )
                    # saving OrderFlpSerializer
                    track_dict_serializer.save(user=request.user, usd_paid_amount=track_usd_paid_amount, jpy_paid_amount=track_jpy_paid_amount)
                    
                    # create a list of tracks to return to frontend
                    purchasedTracksList = []
                    # increment the download count and create list of tracks to return
                    for item in track_dict_serializer.validated_data['track_items']:
                        my_track = Track.objects.get(title=item.get('track').title)
                        my_track.purchase_count += 1
                        purchasedTracksList.append(my_track.pk)
                        my_track.save()
                    # grab a list of all tracks and serialize them
                    tracksForDownload = Track.objects.filter(pk__in=purchasedTracksList)
                    trackDownloadSerializer = TrackSerializer(tracksForDownload, many=True)
                    # only return here if there are no flps to process
                    return Response(trackDownloadSerializer.data, status=status.HTTP_201_CREATED)

            except Exception:
                print('something went wrong with track serializer.save')
                print('here are the track errors')
                print(str(track_dict_serializer.errors))
                print(track_dict_serializer.errors)
                print('here is the track track_dict_serializer')
                print('\n' + str(track_dict_serializer) + '\n')
                # only return if there are no flps to process
                return Response(status=status.HTTP_400_BAD_REQUEST)

    # don't attempt to create serializer for flps if none exists
    if 'no_flps' in str(flp_dict):
        print('\n\nNo flps to process\n\n')
        pass
    else:
        print('\n\nProcessing Flps\n\n')
        # process flp_dict
        flp_dict_serializer = OrderFlpSerializer(data=flp_dict)
    

        if flp_dict_serializer.is_valid():
            usd_paid_amount = 0
            jpy_paid_amount = 0
            # check if this was jpy or usd purchase (usd is default)
            if isUsd:
                for item in flp_dict_serializer.validated_data['flp_items']:
                    if item.get('flp').flp_is_free:
                        print('\nflp ' + str(item.get('flp').flp_name) + ' is a free flp\n')
                        pass
                    else: 
                        usd_paid_amount += item.get('flp').usd_price
            # for jpy
            else:
                for item in flp_dict_serializer.validated_data['flp_items']:
                    if item.get('flp').flp_is_free:
                        print('\flp ' + str(item.get('flp').flp_name) + ' is a free flp\n')
                        pass
                    else: 
                        jpy_paid_amount += item.get('flp').jpy_price
        
            flp_amountStripeWillCharge = int(usd_paid_amount * 100) if isUsd is True else jpy_paid_amount
            
            # if there are tracks and flps to process, process them
            try:
                if not 'no_tracks' in str(track_dict):
                    print('\n Tracks to be processed along with flps\n')
                    stripe.api_key = settings.STRIPE_SK
                    charge = stripe.Charge.create(
                        # if it's usd, stripe takes amount in cents, otherwise leave it whole number for JPY
                        amount = flp_amountStripeWillCharge + track_amountStripeWillCharge,
                        # usd or jpy
                        currency='USD' if isUsd is True else 'JPY',
                        description='Sherrif Crandy flp/audio file digital download charge',
                        # stripe token we get from frontend
                        source=flp_dict_serializer.validated_data['stripe_token']
                    )

                    # save both serializers
                    flp_dict_serializer.save(user=request.user, usd_paid_amount=usd_paid_amount, jpy_paid_amount=jpy_paid_amount)
                    track_dict_serializer.save(user=request.user, usd_paid_amount=track_usd_paid_amount, jpy_paid_amount=track_jpy_paid_amount)
                    
                    # increment both model items
                    for item in flp_dict_serializer.validated_data['flp_items']:
                        my_flp = Flp.objects.get(flp_name=item.get('flp').flp_name)
                        my_flp.purchase_count += 1
                        my_flp.save()
                    for item in track_dict_serializer.validated_data['track_items']:
                        my_track = Track.objects.get(title=item.get('track').title)
                        my_track.purchase_count += 1
                        my_track.save()
                    # pass this to frontend if everything was ok
                    print('\nflp and track data processed together\n')
                    return Response(track_dict_serializer.data, flp_dict_serializer.data, status=status.HTTP_201_CREATED)
                else:
                    print('\n This charge contains flps only\n')
                    stripe.api_key = settings.STRIPE_SK
                    charge = stripe.Charge.create(
                        # if it's usd, stripe takes amount in cents, otherwise leave it whole number for JPY
                        amount = flp_amountStripeWillCharge,
                        # usd or jpy
                        currency='USD' if isUsd is True else 'JPY',
                        description='Sherrif Crandy flp project file download charge',
                        # stripe token we get from frontend
                        source=flp_dict_serializer.validated_data['stripe_token']
                    )

                    # saving OrderFlpSerializer create function
                    flp_dict_serializer.save(user=request.user, usd_paid_amount=usd_paid_amount, jpy_paid_amount=jpy_paid_amount)
                    
                    # create a list of tracks to return to frontend
                    purchasedFlpsList = []
                    for item in flp_dict_serializer.validated_data['flp_items']:
                        my_flp = Flp.objects.get(flp_name=item.get('flp').flp_name)
                        my_flp.purchase_count += 1
                        purchasedFlpsList.append(my_flp.pk)
                        my_flp.save()
                    
                    # grab a list of all flps and serialize them
                    flpsForDownload = Flp.objects.filter(pk__in=purchasedFlpsList)
                    flpDownloadSerializer = FlpSerializer(flpsForDownload, many=True)

                    # pass this to frontend if everything was ok
                    print('\nflp data processed\n')
                    return Response(flpDownloadSerializer.data, status=status.HTTP_201_CREATED)
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

