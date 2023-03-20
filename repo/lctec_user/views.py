from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from lctec_user.models import Cart
from tracks_app.models import Track
from flps_app.models import Flp
from django.contrib.auth import get_user_model
from lctec_user.serializers import *
user = get_user_model()

# checking username in form validation
@api_view(['GET'])
def check_username(request, username):
    username_available = not user.objects.filter(username=username).exists()
    return Response({'available': username_available})

# checking username in form validation
@api_view(['GET'])
def check_email(request, email):
    email_available = not user.objects.filter(email=email).exists()
    return Response({'available': email_available})

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    
    # @csrf_exempt
    # log the user out by deleting their auth token, and save their cart data, if any
    def post(self, request, format=None):


        cart_data = request.data

        # check if cart has data
        if len(cart_data['cart']) == 0:
            print('\nempty cart passed in\n')
        else: 
            print('\nwe have cart data\n')
            # populate track and flp lists from request data
            incoming_tracks_in_cart = [item.get('title')  for item in cart_data.get('cart', []) if 'title' in item]
            print('\nincoming_tracks_in_cart length\n')
            print(str(len(incoming_tracks_in_cart)))
            
            incoming_flps_in_cart = [item.get('flp_name') for item in cart_data.get('cart', []) if 'flp_name' in item]
            print('\nincoming_flps_in_cart length\n')
            print(str(len(incoming_flps_in_cart)))
            # check if this user has a cart object associated with it
            # using this to set cart to None if no object exists instead of raising a DoesNotExist exception
            cart = Cart.objects.filter(user=request.user).first()

            if cart:
                # get all the tracks/flps currently in user's saved cart
                current_tracks_in_cart = [item.title for item in cart.tracks_in_cart.all()]
                current_flps_in_cart = [item.flp_name for item in cart.flps_in_cart.all()]
                
                # if the carts match, there was no change, just log the user out
                if incoming_tracks_in_cart == current_tracks_in_cart and incoming_flps_in_cart == current_flps_in_cart:
                    # delete auth token
                    user = request.user
                    print('\nuser to be logged out: ' + str(request.user) + '\n')
                    Token.objects.filter(user=user).delete()
                    print('\n deleted auth token from user')
                    return Response({'success': 'Logged out successfully.'})
                else:
                    print('\Cart has changed. Updating cart\n')
                    # pass in lists from frontend to get list of track/Flp objs
                    tracks = Track.objects.filter(title__in=incoming_tracks_in_cart)
                    flps = Flp.objects.filter(flp_name__in=incoming_flps_in_cart)
                    print('\n' + str(cart) + '\n')
                    cart.save()
                    cart.tracks_in_cart.set(tracks)
                    cart.flps_in_cart.set(flps)
                    cart.save()
                    # delete auth token
                    user = request.user
                    print('\nuser to be logged out: ' + str(request.user) + '\n')
                    Token.objects.filter(user=user).delete()
                    print('\n deleted auth token from user')
                    return Response({'success': 'Logged out successfully.'})
            
            # user doesn't have cart, create one
            else:
                # pass in lists from frontend to get list of track/Flp objs
                tracks = Track.objects.filter(title__in=incoming_tracks_in_cart)
                flps = Flp.objects.filter(flp_name__in=incoming_flps_in_cart)
                cart = Cart.objects.create(user=request.user)
                print('\n' + str(cart) + '\n')
                cart.save()
                cart.tracks_in_cart.set(tracks)
                cart.flps_in_cart.set(flps)
                cart.save()
                # delete auth token
                user = request.user
                print('\nuser to be logged out: ' + str(request.user) + '\n')
                Token.objects.filter(user=user).delete()
                print('\n deleted auth token from user')
                return Response({'success': 'Logged out successfully.'})

        
        return Response({'success': 'Logged out successfully.'})
    
# get/set auth token
class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = LctecSerializer

    def post(self, request, *args, **kwargs):

        response = super().post(request, *args, **kwargs)
        token = ''
        # first try to get this token (if the user's token was deleted somehow)
        try:
            print('\nattempting to fetch token\n')
            # token = request.user.auth_token
            token = Token.objects.get(key=response.data['token'])
        except:
            # create token for this user:
            print('\ntoken not found. Creating a new token for this user\n')
            token = Token.objects.create(user=request.user)
            print(token.key)

        # get user's cart data
        cart_data = self.get_cart_data(request.user)
        serializer = self.serializer_class(request.user)
        return Response({
            'token': token.key,
            'user': serializer.data,
            'cart': cart_data
        })

    def get_cart_data(self, user):
        cart_items = Cart.objects.filter(user=user)
        cart_data = []
        for item in cart_items:
            if 'title' in item:
                # for tracks
                cart_data.append({
                    'id': item.tracks_in_cart.id,
                    'title': item.tracks_in_cart.product.name,
                })
            if 'flp_name' in item:
                # for tracks
                cart_data.append({
                    'id': item.flps_in_cart.id,
                    'flp_name': item.flps_in_cart.flp_name,
                })

        return cart_data