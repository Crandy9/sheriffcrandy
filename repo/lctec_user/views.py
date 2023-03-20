from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

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
'''
# logging the user out, delete the user's auth token
@api_view(['POST'])
# @authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def lctec_logout(request):
    user = request.user
    print('\nuser to be logged out: ' + str(request.user) + '\n')
    Token.objects.filter(user=user).delete()
    print('\n deleted auth token from user')
    return Response({'success': 'Logged out successfully.'})
'''
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        user = request.user
        print('\nuser to be logged out: ' + str(request.user) + '\n')
        Token.objects.filter(user=user).delete()
        print('\n deleted auth token from user')
        return Response({'success': 'Logged out successfully.'})
