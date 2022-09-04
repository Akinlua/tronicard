

from http import server
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.views.static import serve

urlpatterns = [
    path('troadmin/', admin.site.urls),
    path('', include('blog.urls')),
    path('account/', include('users.urls')),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name= 'reset_password.html'),
        name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name= 'reset_password_sent.html'),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name= 'reset.html'),
         name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name= 'reset_password_complete.html'),
         name="password_reset_complete"),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

