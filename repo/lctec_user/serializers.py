# manually created serializers.py file created to turn DB data into JSON to be used by frontend
from rest_framework import serializers
from .models import *
# import Lctec_user
from django.contrib.auth.models import User


# audio files
# class LcTecSerializer(serializers.ModelSerializer):

#     password = serializers.CharField(
#         min_length=6, write_only=True, required=True)
    
#     class Meta:
#         model = User
#         fields = (
#             'id', 'email', 'password', 'is_staff',
#             'is_active', 'date_joined')

#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)