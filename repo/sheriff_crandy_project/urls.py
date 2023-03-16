from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # djoser library is a REST implementation of Django authentication system
    path('sc/api/v1/', include('djoser.urls')),
    path('sc/api/v1/', include('djoser.urls.authtoken')),
    # include tracks app urls --can check api at http://localhost:8000/api/v1/latest-tracks/
    path('sc/api/v1/', include ('tracks_app.urls')),
    path('sc/api/v1/', include ('flps_app.urls')),
    path('sc/api/v1/', include ('order_app.urls')),
    path('sc/api/v1/', include ('lctec_user.urls')),
] 

# to use media in frontend, not used in live
urlpatterns= urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)