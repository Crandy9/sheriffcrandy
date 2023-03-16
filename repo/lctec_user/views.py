from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth import get_user_model

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