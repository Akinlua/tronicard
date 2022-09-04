from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('create-account/', views.createAccount, name='creatacc'),
    path('profile/', views.account, name= 'account'),
    path('login/', views.loginUser, name= 'login'),
    path('logout/', views.logoutUser, name= 'logout'),
    path('edit-account/', views.editaccount, name= 'editacc'),
]
