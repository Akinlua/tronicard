

from http import server
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings

from django.views.static import serve

urlpatterns = [
    path('troadmin/', admin.site.urls),
    path('', include('blog.urls')),
    path('account/', include('users.urls')),
    

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

