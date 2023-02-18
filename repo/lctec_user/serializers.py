# manually created serializers.py file created to turn DB data into JSON to be used by frontend
from rest_framework import serializers
from .models import *
# import Lctec_user
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()
class LcTecSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = User
        fields = (
            'username, password'
        )
        extra_kwargs = {'password': {'write_only': True, 'required': False}}

    # def create(self, response, validated_data):
    #     print('\n\n\nCREATING USER \n\n\n')
    #     User = get_user_model()
    #     user = User.objects.create_user(response, **validated_data)
    #     return user