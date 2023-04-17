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
    # path('lctec-logout/', views.lctec_logout),
    path('lctec-logout', views.LogoutView.as_view()),
    path('get-cart/', views.get_user_cart),
    path('get-device-data/', views.get_user_device),
    path('send-password-reset-link/', views.send_password_reset_link),
    path('reset-user-password/', views.reset_password)
] 

