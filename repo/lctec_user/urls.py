# manually created urls.py file

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from lctec_user import views

urlpatterns = [
    # for username validation, allow a string to be input as a param
    path('check-username/<str:username>/', views.check_username),
    path('check-email/<str:email>/', views.check_email),
] 

