# manually created serializers.py file created to turn DB data into JSON to be used by frontend
from rest_framework import serializers
from .models import *
# import Lctec_user
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

# return authenticated user as well as user's cart data
User = get_user_model()
class LctecSerializer(serializers.ModelSerializer):
    cart_data = serializers.JSONField()

    class Meta(object):
        model = User
        fields = ('id', 'username', 'email', 'cart_data')
