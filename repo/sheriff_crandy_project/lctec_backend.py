# custom auth backend to allow user to login with either username or email address

from django.db.models import Q

from django.contrib.auth import get_user_model

MyUser = get_user_model()

# called when making api attempts to authenticate users
class Lctec_Backend(object):
    def authenticate(self, request, username=None, password=None, **kwargs):
        print("\n\nbackend accessed\n\n")
        try:
            # Try to fetch the user by searching the username or email field
            user = MyUser.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except MyUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return MyUser.objects.get(pk=user_id)
        except MyUser.DoesNotExist:
            return None