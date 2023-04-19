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
from lctec_user.serializers import *
from django.core.mail import EmailMessage
# converts html template to a string message for emails
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from rest_framework import permissions, status
from django.middleware.csrf import get_token
from django.http import JsonResponse

user = get_user_model()


EMAIL_ON = False
URL = 'http://localhost:8080'



# delete user account
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def delete_user_account_data(request):

    # use first to prevent exception from being raised
    try:

        user_to_be_deleted = user.objects.get(pk=request.user.pk)
        user_to_be_deleted.delete()
        # return no content, everything worked
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    except:
        return Response({'error': 'Invalid token or user'}, status=status.HTTP_400_BAD_REQUEST)



# update user account info
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def update_user_account_data(request):

    # get the user
    current_user = user.objects.get(pk=request.user.pk)
    # Deserialize incoming data
    # serializer = UpdateUserAccountDataSerializer(data=request.data)
    serializer = UpdateUserAccountDataSerializer(data=request.data, context={'request': request})

    if serializer.is_valid():
        # Update user fields
        current_user.username = serializer.validated_data.get('username', current_user.username)
        current_user.email = serializer.validated_data.get('email', current_user.email)
        current_user.first_name = serializer.validated_data.get('first_name', current_user.first_name)
        current_user.last_name = serializer.validated_data.get('last_name', current_user.last_name)
        current_user.favorite_color = serializer.validated_data.get('favorite_color', current_user.favorite_color)

        current_user.save()
        return Response(status=status.HTTP_200_OK)
    else:
        print('\nserializer is not valid')
        print('serializer errors: ' + str(serializer.errors) +  '\n')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# get user account data
@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def get_user_account_data(request):

    current_user = user.objects.get(pk=request.user.pk)
    user_serializer = GetUserSerializer(current_user)
    return Response(user_serializer.data, status=status.HTTP_200_OK)

# reset password
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def reset_password(request):

    try:
        
        uid = force_str(urlsafe_base64_decode(request.data.get('uidb64')))

        current_user = user.objects.get(pk=uid)

    except (TypeError, ValueError, OverflowError, user.DoesNotExist):
        current_user = None

    # Check if the token is valid
    if current_user is not None and default_token_generator.check_token(current_user, request.data.get('token')):
        # Set the new password for the user
        password = request.data.get('password')
        current_user.set_password(password)
        current_user.save()

        template = render_to_string('../templates/changed_account_notice_email.html', {'name':current_user.first_name})
        email = EmailMessage(
            # email subject title default is 'subject'
            'There was a change to your account -- アカウント情報変更のお知らせ',
            # email template default is 'body'
            template,
            # this will be changed to Kaoru's new gmail 
            settings.EMAIL_HOST_USER,
            # recipient list
            [current_user.email],
        )
        email.fail_silently=False
        # eonly send email if this flag is true
        if EMAIL_ON:
            email.send()

        return Response({'success': 'Password reset successful'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid token or user'}, status=status.HTTP_400_BAD_REQUEST)


# send password reset link
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def send_password_reset_link(request):
    
    # get the email address from the POST request
    email = request.data.get('potential_email_address')
    print('\nincoming email: ' + str(email) + '\n\n')

    # check if the email address is valid
    try:
        get_user = user.objects.get(email=email)
        print('\nget_user: ' + str(get_user) + '\n')

        # creating a password reset url unique for each user
        token_generator = PasswordResetTokenGenerator()
        uidb64 = urlsafe_base64_encode(force_bytes(get_user.pk))
        token = token_generator.make_token(get_user)
        # create the password reset URL using the generated token
        password_reset_url = f'{URL}{request.data.get("password_reset_url")}/{uidb64}/{token}/'

        print('\npassword reset url: ' + str(password_reset_url) + '\n')


        EMAIL_ON = True
        template = render_to_string('../templates/password-reset-email.html', {'name':get_user.first_name, 'password_reset_url': password_reset_url})
        email = EmailMessage(
            # email subject title default is 'subject'
            'Password reset -- パスワードのリセット',
            # email template default is 'body'
            template,
            settings.EMAIL_HOST_USER,
            # recipient list
            [get_user.email],
        )
        email.fail_silently=False
        # only send email if this flag is true
        if EMAIL_ON:
            email.send()
        # just return a 200 response
        return HttpResponse(status=200)
    except user.DoesNotExist:
        print('\nUser does not exist\n')
        # handle the case where the user does not exist
        return Response({'error': 'User does not exist'}, status=200)
    
    except Exception as e:
        print('exception:', e)
        return Response({'error': 'Unknown error occurred'}, status=500)


# get user data
@api_view(['GET'])
def get_user_device(request):
    user_agent = request.META.get('HTTP_USER_AGENT', None)    
    print('\nuser_agent: ' + str(user_agent) + '\n')
    # do something with user_ip
    return Response({'message': 'success'})

# get user's cart data after they have authenticated (logged in)
@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def get_user_cart(request):

        # get user's cart data
        cart_data = get_cart_data(request.user)
        return Response({
            'username': request.user.username,
            'cart': cart_data
        })

# get user's cart data, if any
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
# need to include the request or else there will be an error
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