

from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from untitled2 import settings


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('pluk.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
