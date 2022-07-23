from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('create-account/', views.createAccount, name='creatacc'),
    path('', views.account, name= 'account'),
    path('login/', views.loginUser, name= 'login'),
    path('logout/', views.logoutUser, name= 'logout'),
        
]
