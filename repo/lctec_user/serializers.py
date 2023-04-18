# manually created serializers.py file created to turn DB data into JSON to be used by frontend
from rest_framework import serializers
from .models import *
# import Lctec_user
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

# return authenticated user as well as user's cart data
user = get_user_model()



# for updating user account info
class UpdateUserAccountDataSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    favorite_color = serializers.CharField(required=False)

    # automatically called during validation process
    def validate_username(self, value):
        request = self.context.get('request')
        current_user = request.user
        if user.objects.filter(username=value).exists() and current_user.username != value:
            raise serializers.ValidationError('Username already exists.')
        return value

    def validate_email(self, value):
        request = self.context.get('request')
        current_user = request.user
        if user.objects.filter(email=value).exists() and current_user.email != value:
            raise serializers.ValidationError('Email already exists.')
        return value



# for displaying account info to user
class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lctec_User 
        # configure which fields we want to use in frontend. Data is a tuple
        # will be shown in API at DOMAIN/api/v1/latest-tracks/
        fields = (
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "favorite_color"
        )