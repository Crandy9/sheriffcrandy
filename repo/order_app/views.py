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
from tracks_app.serializers import TrackSerializer

# import track and flp models
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
    print('\n\nflag\n\n')
    list_of_files = fileList
    tmp_path = '/tmp/'
    zip_file = zipfile.ZipFile(tmp_path + 'sheriff_crandy_downloadables.zip', 'w')
    # loop through list
    for file in list_of_files:
        print('\nPrinting file in list:\n' + str(file) + '\n')
        # for flps
        if file.endswith('.zip'):
            print('\nCOMPRESSING FLP FILE\n')
            # get the filename only
            fdir, fname = os.path.split(file)
            print('\nWAV FILE NAME fname: ' + str(fname))
            try:
                zip_file.write(str(file), str(fname), compress_type= zipfile.ZIP_DEFLATED)
                print('\n\nSUCCESSFULLY WROTE FLP FILE\n\n')
            except:
                 print('\n\nCOULDNT WRITE FLP FILE\n\n')

        # for tracks
        if file.endswith('.wav'):
            print('\nCOMPRESSING WAV FILE\n')
            # get the filename only
            fdir, fname = os.path.split(file)
            print('\nWAV FILE NAME fname: ' + str(fname))
            try:
                zip_file.write(str(file), str(fname), compress_type= zipfile.ZIP_DEFLATED)
                print('\n\nSUCCESSFULLY WROTE TRACK FILE\n\n')
            except:
                print('\n\nCOULDNT WRITE TRACK FILE\n\n')
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
        print('\n\nNo free tracks to process\n\n')
        pass
    else:
        print('\n\nProcessing free Tracks\n\n')
        # process track_dict
        track_dict_serializer = OrderTrackSerializer(data=track_dict)
        
        if track_dict_serializer.is_valid():

            # if there are free flps to process as well it is a multifile download
            try:
                if not 'no_flps' in str(flp_dict):
                    print('\n free flps need to be processed as well \n')
                    pass
                # else if there are only free tracks to process, create the Stripe charge and save the serializer
                else:
                    print('\nfree tracks only download \n')
                    
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
                            print('\nzip file path:\n' + str(zip) + '\n')
                            # open this zip file and read it
                            with open(zip, 'rb') as f:
                                file_data = f.read()
                            response = HttpResponse(file_data, content_type='application/zip, application/octet-stream')
                            response['Content-Disposition'] = 'attachment; filename=sheriff_crandy_downloadables.zip'
                            print('\n\nsuccessfully opened zip and set response content_type and content-disposition\n\n')
                            # saving OrderFlpSerializer
                            track_dict_serializer.save(user=request.user, free_download=True)
                            os.remove(zip)
                        except:
                            print('\n\nIn freeDownload method, multiple free tracks only. Failed to open zip file as attachment response to axios frontend\n\n')
                            response = HttpResponseNotFound('<h1>File not exist</h1>')

                        return response

                    else:
                        # only return here if there are no flps to process
                        print('\nReturning single free track wav file\n')
                        track_dict_serializer.save(user=request.user, free_download=True)
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
        print('\n\nNo free flps to process\n\n')
        pass
    else:
        print('\n\nProcessing free Flps\n\n')
        # process flp_dict
        flp_dict_serializer = OrderFlpSerializer(data=flp_dict)

        if flp_dict_serializer.is_valid():
            # if there are tracks and flps to process, process them
            try:
                if not 'no_tracks' in str(track_dict):
                    print('\nFree tracks and free flps processed together\n')
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
                    print('\nReturning zip file containing multiple free flps and tracks \n')
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
                        print('\nzip file path:\n' + str(zip) + '\n')
                        # open this zip file and read it
                        with open(zip, 'rb') as f:
                            file_data = f.read()
                        response = HttpResponse(file_data, content_type='application/zip, application/octet-stream')
                        response['Content-Disposition'] = 'attachment; filename=sheriff_crandy_downloadables.zip'
                        print('\n\nsuccessfully opened zip and set response content_type and content-disposition\n\n')
                        # saving OrderFlpSerializer
                        flp_dict_serializer.save(user=request.user, free_download=True)
                        track_dict_serializer.save(user=request.user, free_download=True)
                        os.remove(zip)
                    except:
                        print('\n\nIn freeDownload method, multiple free tracks and free flps. Failed to open zip file as attachment response to axios frontend\n\n')
                        response = HttpResponseNotFound('<h1>File not exist</h1>')
                    print('\n\nreturning zip file as attachment response to axios frontend\n\n')

                    return response
                else:
                    print('\nfree flps only\n')
                    
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
                            print('\nzip file path:\n' + str(zip) + '\n')
                            # open this zip file and read it
                            with open(zip, 'rb') as f:
                                file_data = f.read()
                            response = HttpResponse(file_data, content_type='application/zip, application/octet-stream')
                            response['Content-Disposition'] = 'attachment; filename=sheriff_crandy_downloadables.zip'
                            print('\n\nsuccessfully opened zip and set response content_type and content-disposition\n\n')
                            # saving OrderFlpSerializer
                            flp_dict_serializer.save(user=request.user, free_download=True)
                            os.remove(zip)
                        except:
                            print('\n\nIn freeDownload method, multiple free flps only. Failed to open zip file as attachment response to axios frontend\n\n')
                            response = HttpResponseNotFound('<h1>File not exist</h1>')
                        print('\n\nreturning zip file as attachment response to axios frontend\n\n')

                        return response
                    else:
                        # pass this to frontend if everything was ok
                        flp_dict_serializer.save(user=request.user, free_download=True)
                        print('\rReturn a free single flp zip file\n')
                        return Response(flpDownloadSerializer.data, status=status.HTTP_201_CREATED)
            except Exception:
                print('something went wrong with flp_dict_serializer.save')
                print('here are the track errors')
                print(str(flp_dict_serializer.errors))
                print(flp_dict_serializer.errors)
                print('here is the track flp_dict_serializer')
                print('\n' + str(flp_dict_serializer) + '\n')
                return Response(status=status.HTTP_400_BAD_REQUEST)
    
        # if something is wrong with flp_dict_serializer
        return Response(status=status.HTTP_400_BAD_REQUEST)



    

# when user hits buy button in cart checkout, request comes here
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):

    # bool to check if this is a US or Japan payment
    isUsd = True
    flp_amountStripeWillCharge = 0
    track_amountStripeWillCharge = 0

    flp_dict = request.data
    track_dict = copy.deepcopy(flp_dict)

    # remove irrelevant data from both dicts
    flp_dict.pop('track_items') 
    track_dict.pop('flp_items') 
    
    # don't attempt to create serializer for tracks if none exists
    if 'no_tracks' in str(track_dict):
        print('\n\nNo purchased tracks to process\n\n')
        pass
    else:
        print('\n\nProcessing purchased Tracks\n\n')
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
                    print('\npurchased flps need to be processed as well \n')
                    pass
                # else if there are only tracks to process, create the Stripe charge and save the serializer
                else:
                    print('\nthere are no purchased flps to process \n')
                    stripe.api_key = settings.STRIPE_SK
                    charge = stripe.Charge.create(
                        # if it's usd, stripe takes amount in cents, otherwise leave it whole number for JPY
                        amount = track_amountStripeWillCharge,
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
                        print('\nlen(purchasedTracksList) > 1 is true\n')
                        print('\npurchasedTracksList:\n' + str(purchasedTracksList))
                        try:
                            print('\nIn try block\n')
                            purchasedTracksForZip = []
                            for item in tracksForDownload:
                                print('\nIn for loop iterating over purchasedTracksList\n')
                                # gets the absolute path
                                purchasedTracksForZip.append(item.track.path)
                            print('\nout of for loop\n')
                            print('\nattempting to zip files. Calling createZip method\n')
                            # returns the absolute path of the zipfile
                            zip = createZip(purchasedTracksForZip)
                            print('\nzip file path:\n' + str(zip) + '\n')
                            # open this zip file and read it
                            with open(zip, 'rb') as f:
                                file_data = f.read()
                            response = HttpResponse(file_data, content_type='application/zip, application/octet-stream')
                            response['Content-Disposition'] = 'attachment; filename=sheriff_crandy_downloadables.zip'
                            print('\n\nsuccessfully opened zip and set response content_type and content-disposition\n\n')
                            # saving track_dict_serializer
                            track_dict_serializer.save(user=request.user, usd_paid_amount=track_usd_paid_amount, jpy_paid_amount=track_jpy_paid_amount)                            
                            os.remove(zip)
                        except:
                            print('\n\nIn checkout method, multiple tracks (paid only, or free and paid) only. Failed to open zip file as attachment response to axios frontend\n\n')
                            response = HttpResponseNotFound('<h1>File not exist</h1>')
                        print('\n\nreturning zip file as attachment response to axios frontend\n\n')

                        return response
                    else:
                        # saving track_dict_serializer
                        track_dict_serializer.save(user=request.user, usd_paid_amount=track_usd_paid_amount, jpy_paid_amount=track_jpy_paid_amount)      
                        # only return here if there are no flps to process
                        print('\nReturning a single wav track file\n')
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
                    print('\nPaid tracks to be processed along with flps\n')
                    stripe.api_key = settings.STRIPE_SK
                    charge = stripe.Charge.create(
                        # if it's usd, stripe takes amount in cents, otherwise leave it whole number for JPY
                        amount = flp_amountStripeWillCharge + track_amountStripeWillCharge,
                        # usd or jpy
                        currency='USD' if isUsd is True else 'JPY',
                        description='Sheriff Crandy flp/audio file digital download charge',
                        # stripe token we get from frontend
                        source=flp_dict_serializer.validated_data['stripe_token']
                    )

                    print('Stripe Charge completed')
                    purchasedTracksList = []
                    purchasedFlpList = []
                    # increment both model items
                    for item in flp_dict_serializer.validated_data['flp_items']:
                        print('\nin flp for loop: ' + str(item) + '\n')
                        my_flp = Flp.objects.get(flp_name=item.get('flp').flp_name)
                        my_flp.downloads += 1
                        purchasedFlpList.append(my_flp.pk)
                        my_flp.save()
                    # grab a list of all flps and serialize them
                    flpsForDownload = Flp.objects.filter(pk__in=purchasedFlpList)
                    print('\nlist of flps to be zipped\n')
                    print('\n' + str(flpsForDownload) + '\n')

                    for item in track_dict_serializer.validated_data['track_items']:
                        print('\nin track for loop: ' + str(item) + '\n')
                        my_track = Track.objects.get(title=item.get('track').title)
                        my_track.downloads += 1
                        purchasedTracksList.append(my_track.pk)
                        my_track.save()
                    # grab a list of all flps and serialize them
                    tracksForDownload = Track.objects.filter(pk__in=purchasedTracksList)
                    print('\nlist of tracks to be zipped\n')
                    print('\n' + str(tracksForDownload) + '\n')

                    # Return ZIP files of paid flp/track files
                    print('\nReturning zip file containing multple paid flp and track files\n')
                    try:
                        purchasedTracksAndFlpsForZip = []
                        for mytracks in tracksForDownload:
                            print('\nin tracks loop\n' + str(mytracks) + '\n')
                            # gets the absolute path
                            purchasedTracksAndFlpsForZip.append(mytracks.track.path)
                        for myflps in flpsForDownload:
                            print('\nin flps loop\n' + str(myflps) + '\n')
                            # gets the absolute path
                            purchasedTracksAndFlpsForZip.append(myflps.flp_zip.path)
                        print('\n\nCompleted list of purchased flps and tracks' + str(purchasedTracksAndFlpsForZip) + '\n\n')
                        # returns the absolute path of the zipfile
                        zip = createZip(purchasedTracksAndFlpsForZip)
                        print('\nzip file path:\n' + str(zip) + '\n')
                        # open this zip file and read it
                        with open(zip, 'rb') as f:
                            file_data = f.read()
                        response = HttpResponse(file_data, content_type='application/zip, application/octet-stream')
                        response['Content-Disposition'] = 'attachment; filename=sheriff_crandy_downloadables.zip'
                        print('\n\nsuccessfully opened zip and set response content_type and content-disposition\n\n')
                        # save both serializers
                        flp_dict_serializer.save(user=request.user, usd_paid_amount=usd_paid_amount, jpy_paid_amount=jpy_paid_amount)
                        track_dict_serializer.save(user=request.user, usd_paid_amount=track_usd_paid_amount, jpy_paid_amount=track_jpy_paid_amount)                         
                        os.remove(zip)
                    except:
                        print('\n\nFailed to open zip file as attachment response to axios frontend\n\n')
                        response = HttpResponseNotFound('<h1>File not exist</h1>')
                    print('\n\nreturning zip file as attachment response to axios frontend\n\n')
                    return response
                
                else:
                    print('\nThis charge contains flps only\n')
                    stripe.api_key = settings.STRIPE_SK
                    charge = stripe.Charge.create(
                        # if it's usd, stripe takes amount in cents, otherwise leave it whole number for JPY
                        amount = flp_amountStripeWillCharge,
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
                    print('\nflp data processed\n')
                    if len(purchasedFlpsList) > 1:
                        try:
                            purchasedFlpsForZip = []
                            for item in flpsForDownload:
                                # gets the absolute path
                                purchasedFlpsForZip.append(item.flp_zip.path)
                            # returns the absolute path of the zipfile
                            zip = createZip(purchasedFlpsForZip)
                            print('\nzip file path:\n' + str(zip) + '\n')
                            # open this zip file and read it
                            with open(zip, 'rb') as f:
                                file_data = f.read()
                            response = HttpResponse(file_data, content_type='application/zip, application/octet-stream')
                            response['Content-Disposition'] = 'attachment; filename=sheriff_crandy_downloadables.zip'
                            print('\n\nsuccessfully opened zip and set response content_type and content-disposition\n\n')
                            # save both serializers
                            # saving OrderFlpSerializer create function
                            flp_dict_serializer.save(user=request.user, usd_paid_amount=usd_paid_amount, jpy_paid_amount=jpy_paid_amount)                      
                            os.remove(zip)
                        except:
                            print('\n\nFailed to open zip file as attachment response to axios frontend\n\n')
                            response = HttpResponseNotFound('<h1>File not exist</h1>')
                        print('\n\nreturning zip file as attachment response to axios frontend\n\n')
                        return response

                    else:
                        print('\nReturning zip file containing a single paid flp file\n')
                        flp_dict_serializer.save(user=request.user, usd_paid_amount=usd_paid_amount, jpy_paid_amount=jpy_paid_amount)                      
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

