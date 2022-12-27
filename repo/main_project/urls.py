from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # include muk
    path('api/v1', include('djoser.urls')),
    path('api/v1', include('djoser.urls.authtoken')),
    # include products urls can check api at http://localhost:8000/api/v1/latest-tracks/
    path('api/v1/', include ('products.urls'))
] 
# to use media in frontend, not used in live
urlpatterns= urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)