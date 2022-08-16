
from django.db import models
import uuid
from users.models import Profile

# Create your models here.

class Blog(models.Model):
    owner= models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    title= models.CharField(max_length=200)
    tags= models.ManyToManyField('Tags', blank= True)
    addtag=  models.CharField(max_length=200, null=True, blank=True)
    categories= models.ForeignKey('categories', on_delete=models.SET_NULL, null=True)
    addcategory= models.CharField(max_length=200, null=True)
    blog_image= models.ImageField(default='Tronicard.png' )
    
    body= models.TextField()
    created= models.DateTimeField(auto_now_add=True)
    id= models.UUIDField(default = uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering= ['-created']
    
  

        


class Comments(models.Model):
    owner=models.ForeignKey(Profile, on_delete=models.SET_NULL, null= True)
    name= models.CharField(max_length=500, blank=True)
    reply= models.ForeignKey('self', null=True,on_delete=models.CASCADE, blank=True)
    reply_name=models.CharField(max_length=500, blank=True)
    reply_body=models.TextField(null=True,  blank=True)
    comment_image= models.ImageField(default='userimage.png' )
    body= models.TextField( blank=True)
    blog= models.ForeignKey(Blog, on_delete=models.CASCADE)
    created= models.DateTimeField(auto_now_add=True)
    id= models.UUIDField(default = uuid.uuid4, primary_key=True, unique=True, editable=False)
    def __str__(self):
        return str(self.blog)

    class Meta:
        ordering= ['-created']
    
    def names(self):
        return Comments.objects.filter(name=self)

    def replies(self):
        return Comments.objects.filter(reply=self)

    @property
    def is_reply(self):
        if self.reply is None:
            return False
        return True

class Tags(models.Model):
    name= models.CharField(max_length=200)
    created= models.DateTimeField(auto_now_add=True)
    id= models.UUIDField(default = uuid.uuid4, primary_key=True, unique=True, editable=False)
    def __str__(self):
        return str(self.name)

class Categories(models.Model):
    name= models.CharField(max_length=200, null=True)
    created= models.DateTimeField(auto_now_add=True)
    id= models.UUIDField(default = uuid.uuid4, primary_key=True, unique=True, editable=False)
    def __str__(self):
        return str(self.name)

    class Meta:
        ordering= ['created']