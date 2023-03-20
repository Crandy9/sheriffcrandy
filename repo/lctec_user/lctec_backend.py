# custom auth backend to allow user to login with either username or email address
from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

MyUser = get_user_model()

# called when making api attempts to authenticate users and create auth tokens
class Lctec_Backend(object):
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        print("\n\nbackend accessed for login\n\n")
        try:
            # Try to fetch the user by searching the username or email field
            user = MyUser.objects.get(Q(username=username)|Q(email=username))
            # if password was correct, authenticate using token auth
            if user.check_password(password):

                # create token for this user:
                # first try to get this token (if the user's token was deleted somehow)
                try:
                    print('\nattempting to fetch token\n')
                    token = user.auth_token
                except:
                    print('\ntoken not found. Creating a new token for this user\n')
                    token = Token.objects.create(user=user)
                    print('token data type: '+str(type(token)))
                    print(token.key)
                

                return user
        except MyUser.DoesNotExist:
            return None

    def get_user(self, user_id):

        print('get user function')
        try:
            return MyUser.objects.get(pk=user_id)
        except MyUser.DoesNotExist:
            return None
        