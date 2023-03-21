from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from lctec_user.models import Cart
from tracks_app.models import Track
from flps_app.models import Flp
from django.contrib.auth import get_user_model
from tracks_app.serializers import TrackSerializer
from flps_app.serializers import FlpSerializer


user = get_user_model()


# get user's cart data after they have authenticated (logged in)
@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def get_user_cart(request):

        # get user's cart data
        cart_data = get_cart_data(request.user)
        return Response({
            'cart': cart_data
        })

def get_cart_data(user):
    # get the cart, use filter().first() to avoid NotFound error. 
    # will return None if not found
    cart = Cart.objects.filter(user=user).first()
    cart_data = []
    if cart:
        # get all the track cart items via serializer
        for item in cart.tracks_in_cart.all():
            track_serializer = TrackSerializer(item)
            cart_data.append(track_serializer.data)
        for item in cart.flps_in_cart.all():
            flp_serializer = FlpSerializer(item)
            cart_data.append(flp_serializer.data)

    return cart_data

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

# de-authenticate user by deleting auth token, and storing/updating and then saving the user's cart data
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, format=None):

        cart_data = request.data

        # populate track and flp lists from request data
        incoming_tracks_in_cart = [item.get('title')  for item in cart_data.get('cart', []) if 'title' in item]
        
        incoming_flps_in_cart = [item.get('flp_name') for item in cart_data.get('cart', []) if 'flp_name' in item]
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
                Token.objects.filter(user=user).delete()
                return Response({'success': 'Logged out successfully.'})
            else:
                # pass in lists from frontend to get list of track/Flp objs
                tracks = Track.objects.filter(title__in=incoming_tracks_in_cart)
                flps = Flp.objects.filter(flp_name__in=incoming_flps_in_cart)
                cart.save()
                cart.tracks_in_cart.set(tracks)
                cart.flps_in_cart.set(flps)
                cart.save()
                # delete auth token
                user = request.user
                Token.objects.filter(user=user).delete()
                return Response({'success': 'Logged out successfully.'})
        
        # user doesn't have cart, create one
        else:
            # pass in lists from frontend to get list of track/Flp objs
            tracks = Track.objects.filter(title__in=incoming_tracks_in_cart)
            flps = Flp.objects.filter(flp_name__in=incoming_flps_in_cart)
            cart = Cart.objects.create(user=request.user)
            cart.save()
            cart.tracks_in_cart.set(tracks)
            cart.flps_in_cart.set(flps)
            cart.save()
            # delete auth token
            user = request.user
            Token.objects.filter(user=user).delete()
            return Response({'success': 'Logged out successfully.'})

        
    
