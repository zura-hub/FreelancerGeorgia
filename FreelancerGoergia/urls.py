from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('jobs/', include('jobs.urls')),
    path('accounts/', include('accounts.urls')),
    path('freelacersProfiles/', include('freelacersProfiles.urls')),
<<<<<<< HEAD
    path('templates/', include('templates.urls')),
    path('resset/', include('resset.urls')),
=======
    
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
>>>>>>> 4bd70acf3b4265b9caba25c855ca94d1e597a374

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)