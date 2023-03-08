from django.urls import path

from order_app import views

urlpatterns = [
    # not sure about this path
    path('checkout/', views.checkout),
    path('freeDownload/', views.freeDownload)
]