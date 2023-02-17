from django.shortcuts import render

# https://stackoverflow.com/questions/33674373/django-custom-user-model-password-is-not-being-hashed
# class SignUpView(views.APIView):
#     authentication_classes = ()
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request, format=None):
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)