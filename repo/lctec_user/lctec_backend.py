# custom auth backend to allow user to login with either username or email address
from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

lctec_user = get_user_model()

# called when making api attempts to authenticate users and create auth tokens
class Lctec_Backend(object):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Try to fetch the user by searching the username or email field
            user = lctec_user.objects.get(Q(username=username)|Q(email=username))
            # if password was correct, authenticate using token auth
            if user.check_password(password):

                # create token for this user:
                # first try to get this token (if the user's token was deleted somehow)
                try:
                    token = user.auth_token
                except:
                    token = Token.objects.create(user=user)
                

                return user
        except lctec_user.DoesNotExist:
            return None

    # called when saving a new model obj
    def get_user(self, user_id):

        try:
            print('\n\ncurrent user: ' + str(lctec_user.objects.get(pk=user_id)))
            return lctec_user.objects.get(pk=user_id)
        except lctec_user.DoesNotExist:
            return None
        