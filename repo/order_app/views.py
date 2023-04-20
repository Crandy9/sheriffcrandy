# to talk to Stripe API
from django import views
from django.http import HttpResponse, HttpResponseNotFound
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
from tracks_app.serializers import TrackSerializer, GetPurchasedTrackSerializer

# import track and flp models
from order_app.models import *
from flps_app.models import *
from tracks_app.models import *

# import copy module to allow creating two dicts one for tracks and one for flps
import copy

# import modules to zip up multiple files
import zipfile


# zip up mulitple files
# sample: https://stackoverflow.com/questions/12881294/django-create-a-zip-of-multiple-files-and-make-it-downloadable
# https://www.youtube.com/watch?v=6HjHPvmwiSs
def createZip(fileList):
    list_of_files = fileList
    tmp_path = '/tmp/'
    zip_file = zipfile.ZipFile(tmp_path + 'sheriff_crandy_downloadables.zip', 'w')
    # loop through list
    for file in list_of_files:
        # for flps
        if file.endswith('.zip'):
            # get the filename only
            fdir, fname = os.path.split(file)
            try:
                zip_file.write(str(file), str(fname), compress_type= zipfile.ZIP_DEFLATED)
            except:
                 return

        # for tracks
        if file.endswith('.wav'):
            # get the filename only
            fdir, fname = os.path.split(file)
            try:
                zip_file.write(str(file), str(fname), compress_type= zipfile.ZIP_DEFLATED)
            except:
                return
    zip_file.close()
    return (tmp_path + 'sheriff_crandy_downloadables.zip')


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
# process order but don't make stripe charges
def freeDownload(request):
        
    flp_dict = request.data
    track_dict = copy.deepcopy(flp_dict)

    # remove irrelevant data from both dicts
    flp_dict.pop('track_items') 
    track_dict.pop('flp_items') 

    
    # don't attempt to create serializer for tracks if none exists
    if 'no_tracks' in str(track_dict):
        pass
    else:
        # process track_dict
        track_dict_serializer = OrderTrackSerializer(data=track_dict)
        if track_dict_serializer.is_valid():

            # if there are free flps to process as well it is a multifile download
            try:
                if not 'no_flps' in str(flp_dict):
                    pass
                # else if there are only free tracks to process, create the Stripe charge and save the serializer
                else:
                    
                    # create a list of tracks to return to frontend
                    freedownloadTracksList = []
                    # increment the download count and create list of tracks to return
                    for item in track_dict_serializer.validated_data['track_items']:
                        my_track = Track.objects.get(title=item.get('track').title)
                        my_track.downloads += 1
                        freedownloadTracksList.append(my_track.pk)
                        my_track.save()
                    
                    # grab a list of all tracks and serialize them
                    tracksForDownload = Track.objects.filter(pk__in=freedownloadTracksList)
                    trackDownloadSerializer = TrackSerializer(tracksForDownload, many=True)

                    # if there are more than one tracks being downloaded, zip them up and return the zip file
                    if len(freedownloadTracksList) > 1:
                        try:
                            freeTracksForZip = []
                            for item in tracksForDownload:
                                # gets the absolute path
                                freeTracksForZip.append(item.track.path)

                            # returns the absolute path of the zipfile
                            zip = createZip(freeTracksForZip)
                            # open this zip file and read it
                            with open(zip, 'rb') as f:
                                file_data = f.read()
                            response = HttpResponse(file_data, content_type='application/zip, application/octet-stream')
                            response['Content-Disposition'] = 'attachment; filename=sheriff_crandy_downloadables.zip'
                            # saving OrderFlpSerializer
                            track_dict_serializer.save(user=request.user, free_download=True)
                            os.remove(zip)
                        except:
                            response = HttpResponseNotFound('<h1>File not exist</h1>')

                        return response

                    else:
                        # only return here if there are no flps to process
                        track_dict_serializer.save(user=request.user, free_download=True)
                        return Response(trackDownloadSerializer.data, status=status.HTTP_201_CREATED)

            except Exception:
                # only return if there are no flps to process
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # don't attempt to create serializer for flps if none exists
    if 'no_flps' in str(flp_dict):
        pass
    else:
        # process flp_dict
        flp_dict_serializer = OrderFlpSerializer(data=flp_dict)

        if flp_dict_serializer.is_valid():
            # if there are tracks and flps to process, process them
            try:
                if not 'no_tracks' in str(track_dict):
                    freeDownloadedFlpsList = []
                    freedownloadTracksList = []
                    # increment both model items
                    for item in flp_dict_serializer.validated_data['flp_items']:
                        my_flp = Flp.objects.get(flp_name=item.get('flp').flp_name)
                        my_flp.downloads += 1
                        freeDownloadedFlpsList.append(my_flp.pk)
                        my_flp.save()
                    for item in track_dict_serializer.validated_data['track_items']:
                        my_track = Track.objects.get(title=item.get('track').title)
                        my_track.downloads += 1
                        freedownloadTracksList.append(my_track.pk)
                        my_track.save()
                    # pass zip file containing all free downloaded items
                    try:
                        tracksAndFlpsForZip = []
                        for item in freeDownloadedFlpsList:
                            # gets the absolute path
                            tracksAndFlpsForZip.append(item.track.path)
                        for item in freedownloadTracksList:
                            # gets the absolute path
                            tracksAndFlpsForZip.append(item.flp_zip.path)
                        # returns the absolute path of the zipfile
                        zip = createZip(tracksAndFlpsForZip)
                        # open this zip file and read it
                        with open(zip, 'rb') as f:
                            file_data = f.read()
                        response = HttpResponse(file_data, content_type='application/zip, application/octet-stream')
                        response['Content-Disposition'] = 'attachment; filename=sheriff_crandy_downloadables.zip'
                        # saving OrderFlpSerializer
                        flp_dict_serializer.save(user=request.user, free_download=True)
                        track_dict_serializer.save(user=request.user, free_download=True)
                        os.remove(zip)
                    except:
                        response = HttpResponseNotFound('<h1>File not exist</h1>')

                    return response
                else:
                    
                    # create a list of tracks to return to frontend
                    freeDownloadedFlpsList = []
                    for item in flp_dict_serializer.validated_data['flp_items']:
                        my_flp = Flp.objects.get(flp_name=item.get('flp').flp_name)
                        my_flp.downloads += 1
                        freeDownloadedFlpsList.append(my_flp.pk)
                        my_flp.save()
                    
                    # grab a list of all flps and serialize them
                    flpsForDownload = Flp.objects.filter(pk__in=freeDownloadedFlpsList)
                    flpDownloadSerializer = FlpSerializer(flpsForDownload, many=True)

                    # check if there are multiple free flps being downloaded
                    if len(freeDownloadedFlpsList) > 1:
                        try:
                            freeFlpsForZip = []
                            for item in flpsForDownload:
                                # gets the absolute path
                                freeFlpsForZip.append(item.flp_zip.path)

                            # returns the absolute path of the zipfile
                            zip = createZip(freeFlpsForZip)
                            # open this zip file and read it
                            with open(zip, 'rb') as f:
                                file_data = f.read()
                            response = HttpResponse(file_data, content_type='application/zip, application/octet-stream')
                            response['Content-Disposition'] = 'attachment; filename=sheriff_crandy_downloadables.zip'
                            # saving OrderFlpSerializer
                            flp_dict_serializer.save(user=request.user, free_download=True)
                            os.remove(zip)
                        except:
                            response = HttpResponseNotFound('<h1>File not exist</h1>')

                        return response
                    else:
                        # pass this to frontend if everything was ok
                        flp_dict_serializer.save(user=request.user, free_download=True)
                        return Response(flpDownloadSerializer.data, status=status.HTTP_201_CREATED)
            except Exception:
                return Response(status=status.HTTP_400_BAD_REQUEST)
    
        # if something is wrong with flp_dict_serializer
        return Response(status=status.HTTP_400_BAD_REQUEST)


# when user hits buy button in cart checkout, request comes here
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):


    # bool to check if this is a US or Japan payment
    isUsd = None
    # flp_amountStripeWillCharge = 0
    # track_amountStripeWillCharge = 0
    TOTAL_USD_PAID = float(str(request.data.pop('usd_paid_amount')).strip(' "'))
    TOTAL_JPY_PAID = int(str(request.data.pop('jpy_paid_amount')).strip(' "'))
    # check if this is a usd or jpy purchase
    if TOTAL_JPY_PAID > 1:
        isUsd = False
    else:
        isUsd = True

    flp_dict = request.data
    track_dict = copy.deepcopy(flp_dict)


    # remove irrelevant data from both dicts
    flp_dict.pop('track_items') 
    track_dict.pop('flp_items') 
    
    # don't attempt to create serializer for tracks if none exists
    if 'no_tracks' in str(track_dict):
        pass
    else:
        # process track_dict
        track_dict_serializer = OrderTrackSerializer(data=track_dict)
        
        if track_dict_serializer.is_valid():

            # if there are flps to process, don't create stripe charge or return any data yet
            try:
                if not 'no_flps' in str(flp_dict):
                    pass
                # else if there are only tracks to process, create the Stripe charge and save the serializer
                else:
                    stripe.api_key = settings.STRIPE_SK
                    charge = stripe.Charge.create(
                        # if it's usd, stripe takes amount in cents, otherwise leave it whole number for JPY
                        amount = int(TOTAL_USD_PAID * 100) if isUsd is True else TOTAL_JPY_PAID,
                        # usd or jpy
                        currency='USD' if isUsd is True else 'JPY',
                        description='Sheriff Crandy digital audio track download charge',
                        # stripe token we get from frontend
                        source=track_dict_serializer.validated_data['stripe_token']
                    )

                    
                    # create a list of tracks to return to frontend
                    purchasedTracksList = []
                    # increment the download count and create list of tracks to return
                    for item in track_dict_serializer.validated_data['track_items']:
                        my_track = Track.objects.get(title=item.get('track').title)
                        my_track.downloads += 1
                        purchasedTracksList.append(my_track.pk)
                        my_track.save()
                    # grab a list of all tracks and serialize them
                    tracksForDownload = Track.objects.filter(pk__in=purchasedTracksList)
                    trackDownloadSerializer = TrackSerializer(tracksForDownload, many=True)

                    # check for multiple files
                    if len(purchasedTracksList) > 1:
                        try:
                            purchasedTracksForZip = []
                            for item in tracksForDownload:
                                # gets the absolute path
                                purchasedTracksForZip.append(item.track.path)
                            # returns the absolute path of the zipfile
                            zip = createZip(purchasedTracksForZip)
                            # open this zip file and read it
                            with open(zip, 'rb') as f:
                                file_data = f.read()
                            response = HttpResponse(file_data, content_type='application/zip, application/octet-stream')
                            response['Content-Disposition'] = 'attachment; filename=sheriff_crandy_downloadables.zip'
                            # saving track_dict_serializer
                            track_dict_serializer.save(user=request.user, usd_paid_amount=TOTAL_USD_PAID, jpy_paid_amount=TOTAL_JPY_PAID)                            
                            os.remove(zip)
                        except:
                            response = HttpResponseNotFound('<h1>File not exist</h1>')

                        return response
                    else:
                        # saving track_dict_serializer
                        track_dict_serializer.save(user=request.user, usd_paid_amount=TOTAL_USD_PAID, jpy_paid_amount=TOTAL_JPY_PAID)      
                        # only return here if there are no flps to process
                        return Response(trackDownloadSerializer.data, status=status.HTTP_201_CREATED)

            except Exception:
                # only return if there are no flps to process
                return Response(status=status.HTTP_400_BAD_REQUEST)

    # don't attempt to create serializer for flps if none exists
    if 'no_flps' in str(flp_dict):
        pass
    else:
        # process flp_dict
        flp_dict_serializer = OrderFlpSerializer(data=flp_dict)
    

        if flp_dict_serializer.is_valid():
            # if there are tracks and flps to process, process them
            try:
                if not 'no_tracks' in str(track_dict):
                    stripe.api_key = settings.STRIPE_SK
                    charge = stripe.Charge.create(
                        # if it's usd, stripe takes amount in cents, otherwise leave it whole number for JPY
                        amount = int(TOTAL_USD_PAID * 100) if isUsd is True else TOTAL_JPY_PAID,
                        # usd or jpy
                        currency='USD' if isUsd is True else 'JPY',
                        description='Sheriff Crandy flp/audio file digital download charge',
                        # stripe token we get from frontend
                        source=flp_dict_serializer.validated_data['stripe_token']
                    )

                    purchasedTracksList = []
                    purchasedFlpList = []
                    # increment both model items
                    for item in flp_dict_serializer.validated_data['flp_items']:
                        my_flp = Flp.objects.get(flp_name=item.get('flp').flp_name)
                        my_flp.downloads += 1
                        purchasedFlpList.append(my_flp.pk)
                        my_flp.save()
                    # grab a list of all flps and serialize them
                    flpsForDownload = Flp.objects.filter(pk__in=purchasedFlpList)

                    for item in track_dict_serializer.validated_data['track_items']:
                        my_track = Track.objects.get(title=item.get('track').title)
                        my_track.downloads += 1
                        purchasedTracksList.append(my_track.pk)
                        my_track.save()
                    # grab a list of all flps and serialize them
                    tracksForDownload = Track.objects.filter(pk__in=purchasedTracksList)

                    # Return ZIP files of paid flp/track files
                    try:
                        purchasedTracksAndFlpsForZip = []
                        for mytracks in tracksForDownload:
                            # gets the absolute path
                            purchasedTracksAndFlpsForZip.append(mytracks.track.path)
                        for myflps in flpsForDownload:
                            # gets the absolute path
                            purchasedTracksAndFlpsForZip.append(myflps.flp_zip.path)
                        # returns the absolute path of the zipfile
                        zip = createZip(purchasedTracksAndFlpsForZip)
                        # open this zip file and read it
                        with open(zip, 'rb') as f:
                            file_data = f.read()
                        response = HttpResponse(file_data, content_type='application/zip, application/octet-stream')
                        response['Content-Disposition'] = 'attachment; filename=sheriff_crandy_downloadables.zip'
                        # save both serializers but only give one order the total
                        flp_dict_serializer.save(user=request.user)
                        track_dict_serializer.save(user=request.user, usd_paid_amount=TOTAL_USD_PAID, jpy_paid_amount=TOTAL_JPY_PAID)                         
                        os.remove(zip)
                    except:
                        response = HttpResponseNotFound('<h1>File not exist</h1>')
                    return response
                
                else:
                    stripe.api_key = settings.STRIPE_SK
                    charge = stripe.Charge.create(
                        # if it's usd, stripe takes amount in cents, otherwise leave it whole number for JPY
                        amount = int(TOTAL_USD_PAID * 100) if isUsd is True else TOTAL_JPY_PAID,
                        # usd or jpy
                        currency='USD' if isUsd is True else 'JPY',
                        description='Sheriff Crandy flp project file download charge',
                        # stripe token we get from frontend
                        source=flp_dict_serializer.validated_data['stripe_token']
                    )
                    
                    # create a list of tracks to return to frontend
                    purchasedFlpsList = []
                    for item in flp_dict_serializer.validated_data['flp_items']:
                        my_flp = Flp.objects.get(flp_name=item.get('flp').flp_name)
                        my_flp.downloads += 1
                        purchasedFlpsList.append(my_flp.pk)
                        my_flp.save()
                    
                    # grab a list of all flps and serialize them
                    flpsForDownload = Flp.objects.filter(pk__in=purchasedFlpsList)
                    flpDownloadSerializer = FlpSerializer(flpsForDownload, many=True)

                    # pass this to frontend if everything was ok
                    if len(purchasedFlpsList) > 1:
                        try:
                            purchasedFlpsForZip = []
                            for item in flpsForDownload:
                                # gets the absolute path
                                purchasedFlpsForZip.append(item.flp_zip.path)
                            # returns the absolute path of the zipfile
                            zip = createZip(purchasedFlpsForZip)
                            # open this zip file and read it
                            with open(zip, 'rb') as f:
                                file_data = f.read()
                            response = HttpResponse(file_data, content_type='application/zip, application/octet-stream')
                            response['Content-Disposition'] = 'attachment; filename=sheriff_crandy_downloadables.zip'
                            # save both serializers
                            # saving OrderFlpSerializer create function
                            flp_dict_serializer.save(user=request.user, usd_paid_amount=TOTAL_USD_PAID, jpy_paid_amount=TOTAL_JPY_PAID)                      
                            os.remove(zip)
                        except:
                            response = HttpResponseNotFound('<h1>File not exist</h1>')
                        return response

                    else:
                        flp_dict_serializer.save(user=request.user, usd_paid_amount=TOTAL_USD_PAID, jpy_paid_amount=TOTAL_JPY_PAID)                      
                        return Response(flpDownloadSerializer.data, status=status.HTTP_201_CREATED)
            except Exception:
                return Response(status=status.HTTP_400_BAD_REQUEST)
    
        # if something is wrong with flp_dict_serializer
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

# get user track orders to unlock full song
# pass in the user, get a list of tracks that they bought
@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def get_track_orders(request):
    user = request.user
    # will return None if not found
    order_track_items = OrderTrackItem.objects.filter(order__user=user).select_related('track')
    track_ids = [item.track.id for item in order_track_items]
    tracks = Track.objects.filter(id__in=track_ids)
    # if the user hasn't bought any tracks, return an empty list
    if not tracks: # check if queryset is empty
        return Response([])
    # convert these objects into JSON. Pass in tracks and set many=True because we have more than one obj
    serializer = GetPurchasedTrackSerializer(tracks, many=True)

    return Response(serializer.data)