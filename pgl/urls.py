
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static # image upload
from django.conf import settings  # image upload


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
]


if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

