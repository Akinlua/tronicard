from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('create-blog/', views.createBlog, name='createblog'),
    # # path('delete-blog/', views.createBlog, name='deleteblog'),
    # # path('about-us/', views.createBlog, name='aboutus'),
    path('blog/', views.blog, name='blog'),
    path('single-blog/<str:pk>/', views.singleBlog, name='singleblog'),
    path('pagenotfound/', views.exitNot, name='pagenot'),
    path('deletePost/<str:pk>/', views.deletePost, name='deletepost'),
    path('updateBlog/<str:pk>/', views.updateBlog, name='updateblog'),
    path('loadmore/', views.loadmore, name='loadmore'),
    path('createForm/', views.createCommentForm, name='createform'),
    path('replyform/', views.replyform, name='replyform'),
    path('deletecomment/<str:pk>/', views.deletecomment, name='deletecomment'),
    

]
