
# Create your views here.

from tkinter import Image
from unittest import result
from django.utils.datastructures import MultiValueDictKeyError
from urllib import request
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from tkinter.messagebox import RETRY
from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect
from .form import BlogForm, CommentForm
from .models import Blog, Comments, Tags, Categories
from .utils import searchStuff, sideBlog, disorder_Blog, paginateQuery
from django.core.paginator import Paginator
from random import shuffle
from django.contrib import messages
from django.views.generic import View
from django.http import JsonResponse, HttpResponse
from django.core import serializers

def about(request):
    return render(request, 'about.html')
def home(request):


    blog,q= searchStuff(request)
    banner_blog= Blog.objects.all()
    banner_blog=disorder_Blog(banner_blog)
    banner_blog=sideBlog(banner_blog,10)
    # disorder_blog=disorder_Blog(blog)

    disorder_blog= sideBlog(blog, 12)
    sideblog=Blog.objects.all()
    sideblog= sideBlog(sideblog, 5)
    
    tags= Tags.objects.all()
    categories= Categories.objects.all()
    # disorder_blog, customRange=paginateQuery(request, blog, 5)
    
    context={'blogs':disorder_blog, 'banner_blog':banner_blog, 'q':q, 'sidebl':sideblog, 'tags':tags, 'categories':categories}
    return render(request, 'home.html', context)

def exitNot(request):
    return render(request, 'blog/exitnot.html')
    
@login_required(login_url='login')
def createBlog(request):
    try:
        admin = request.user.profile.is_admin
    except:
        admin = None
    if admin:
        form = BlogForm()

        if request.method == 'POST':
            form=BlogForm(request.POST, request.FILES)
            if form.is_valid():
                
                blog=form.save(commit=False)
                blog.addcategory=blog.addcategory.lower()
                if blog.categories.name == 'None' and blog.addcategory == 'none':
                    messages.error(request, 'Make sure you add a category')
                else:
                    blog.save()
                    return redirect('home')
            
        context={'form':form}
        return render(request, 'blog/create-blog.html', context)
    else:
        return redirect('pagenot')

def blog(request):

    blog,q= searchStuff(request) 
    sideblog= sideBlog(blog, 5)
    # disorder_blog=disorder_Blog(blog)
    blogs, customRange= paginateQuery(request, blog, 12)
    
    tags= Tags.objects.all()
    categories= Categories.objects.all()
    
    context={'categories':categories, 'tags':tags, 'customRange':customRange,'blogs':blogs, 'q':q, 'sidebl':sideblog}
    return render(request, 'blog/blog.html', context)
def deletecomment(request, pk):
    try:
        user = request.user.profile
    except:
        user = None
    if user:
        comment = Comments.objects.get(id=pk)
        if  request.user.profile.name == comment.name:
            comment.delete()
        else:
            return redirect('pagenot')
        return redirect(request.GET['next'] if 'next' in request.GET else 'home')
    else:
        return redirect('pagenot')

def singleBlog(request, pk):
    blogs,q= searchStuff(request) 
    sideblog= sideBlog(blogs, 5)

    tags= Tags.objects.all()
    categories= Categories.objects.all()
    blog = Blog.objects.get(id=pk)
    
    try:
        user= request.user.profile
    except:
        user = None
    
    form = CommentForm()
    
    comments= blog.comments_set.all()[0:5]
    
    try:
        reply_id=request.POST.get('reply_id')
    except:
        reply_id=None
    if reply_id:
        reply_obj=Comments.objects.filter(id=reply_id)
        if reply_obj.exists():
            reply_obj=reply_obj.first()
    if request.method == 'POST':
        form= CommentForm(request.POST)
        if form.is_valid():
            comme=form.save(commit=False)
            comme.blog= blog
            if reply_id:
                comme.owner= user
                comme.reply= reply_obj
                comme.reply_name=comme.reply_name
                comme.reply_body= comme.reply_body
                comme.comment_image= comme.comment_image
                if user:
                    comme.reply_name=user.name
                    comme.comment_image= user.image
                
            else:
                if user:
                    comme.name= user.name
                    comme.owner= user
                    comme.comment_image= user.image
            
            comme.save()
        
            return redirect('singleblog', pk= blog.id)
        
    
    
    comment_count= blog.comments_set.all().count()
    context={'categories':categories,'tags':tags, 'blog':blog, 'q':q, 'blogs': blogs, 'form': form, 'comments': comments,'comment_count':comment_count, 'sidebl':sideblog}
    return render(request, 'blog/post-details.html', context)


def createCommentForm(request):

    # try:
    #     reply_id=request.POST.get('reply_id')
    # except:
    #     reply_id=None
    # if reply_id:
    #     reply_obj=Comments.objects.filter(id=reply_id)
    #     if reply_obj.exists():
    #         reply_obj=reply_obj.first()
    # if reply_id:
    #         reply= reply_obj
    # else:
    #     reply=None
    # dont need

    try:
        user= request.user.profile
    except:
        user = None
       
    
    if user:
        owner= user
        comment_image=user.image
    else:
        owner=None
        comment_image=None
    if request.method == 'POST':
        blog_id= request.POST['blog_id']
        blog = Blog.objects.get(id=blog_id)
        name= request.POST['name']
        body= request.POST['body']
        if name=="":
            name = None
        if name:
            name=name
        else:
            if user:
                name=user.name
       
            
        if name != "":
            if body != "":
                if comment_image == None:
                    comment= Comments.objects.create(
                        owner= owner,
                        name=name,
                        body=body,
                        blog= blog,
                    )
                else:
                    comment= Comments.objects.create(
                        owner= owner,
                        name=name,
                        comment_image=comment_image,
                        body=body,
                        blog= blog,
                    )
        
                comment.save()

                comments= blog.comments_set.all()
                comment_count= blog.comments_set.all().count()
                
                # serialize in new friend object in json
                ser_comment = serializers.serialize('json', comments)
                # send to client side.
                return JsonResponse({"comments": ser_comment,'comment_count':comment_count}, status=200)
        
        # sucess='done'
        # data={}
        # comment_json=serializers.serialize('json', comments)
        # return JsonResponse(data={
        #     'comments':comment_json,
        #     'sucess':sucess,
            
        # })
    
def replyform(request):
    if request.method == 'POST':
        try:
            reply_id=request.POST.get('reply_id')
        except:
            reply_id=None
        # reply_id= request.POST['reply_id']
        print(reply_id)
        if reply_id:
            reply_obj=Comments.objects.filter(id=reply_id)
            if reply_obj.exists():
                reply_obj=reply_obj.first()
        if reply_id:
                reply= reply_obj
        else:
            reply=None
        # dont need

        try:
            user= request.user.profile
        except:
            user = None
        
        
        if user:
            owner= user
            comment_image=user.image
        
    
        blog_id= request.POST['blog_id']
        blog = Blog.objects.get(id=blog_id)
        name= request.POST['name']
        body= request.POST['body']
        if name=="":
            name=None
        if name:
            name=name
        else:
            if user:
                name=user.name
       
            
        if name:
            if body:
                comment= Comments.objects.create(
                    owner= owner,
                    name=name,
                    comment_image=comment_image,
                    body=body,
                    blog= blog,
                )
        
        
        comment.save()
        comments=blog.comments_set.all()
        
        total_data= comments.count()
        print(total_data)
        # serialize in new friend object in json
        ser_comment = serializers.serialize('json', comments)
        # send to client side.
        return JsonResponse({"comments": ser_comment, 'total_data:':total_data,}, status=200)
    

@login_required(login_url='login')
def deletePost(request, pk):
    try:
        admin = request.user.profile.is_admin
    except:
        admin = None
    if admin:
        blog = Blog.objects.get(id=pk)
        blog.delete()
        return redirect(request.GET['next'] if 'next' in request.GET else 'home')
    else:
        return redirect('pagenot')

def loadmore(request):
    # offset = request.POST.get('is_private', False)
    offset=int(request.POST['offset'])
    print(offset)
    blog_id=request.POST['blog_id']
    add_div=5
    blog=Blog.objects.get(id=blog_id)
    comments=blog.comments_set.all()[offset:offset+add_div]
    total_data=blog.comments_set.all().count()
    
    data={}
    comment_json=serializers.serialize('json', comments)
    return JsonResponse(data={
        'comment':comment_json,
        'totalResult':total_data,
    })

    

# def makeComment(request):
#     blog = Blog.objects.get(id=pk)
#     comments= blog.comments_set.all()
#     form = CommentForm()

#     comment_count= blog.comments_set.all().count()
#     if request.method == 'POST':
#         form= CommentForm(request.POST)
#         if form.is_valid():
#             comme=form.save(commit=False)
#             comme.blog= blog
#             comme.save()

#     return render(request, 'blog/post-details.html', context)


# # def editBlog()

# # def deleteBlog()

# try:
#         reply_id=request.POST.get('reply_id')
#     except:
#         reply_id=None
#     if reply_id:
#         reply_obj=Comments.objects.filter(id=reply_id)
#         if reply_obj.exists():
#             reply_obj=reply_obj.first()
#     try:
#         user= request.user.profile
#     except:
#         user = None
            
#     blog_id=request.POST.get('blog_id')
#     blog=Blog.objects.get(id=blog_id)
#     if reply_id:
#             reply= reply_obj
#     else:
#         reply=None
    
#     if user:
#         owner= user
#         comment_image=user.image
        
#     if request.method == 'POST':
#         name= request.POST['name']
#         body= request.POST['body']
#         if name:
#             name=name
#         else:
#             if user:
#                 name=user.name
       
            
#         if name:
#             if body:
#                 comment= Comments.objects.create(
#                     owner= owner,
#                     name=name,
#                     reply= reply,
#                     comment_image=comment_image,
#                     body=body,
#                     blog= blog,
#                 )
#         comment.save()
#         return HttpResponse()