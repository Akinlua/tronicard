from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User

from .models import Tags, Blog, Categories


from django.conf import settings

def updateTag(sender, instance, created, **kwargs):
    if created:
        blog=instance
        if blog.addtag:
                tags=blog.addtag
                tags= tags.split()
                tagie= Tags.objects.all()
                tagies=[]
                for cat in tagie:
                    tagies.append(cat.name)
                    
                for tag in tags:
                    if tag in tagies:
                        tags.remove(tag)

                for tag in tags:
                    tags_=Tags.objects.create(
                        name=tag
                    )
    

def updateCategory(sender, instance, created, **kwargs):
    if created:
        blog=instance 
        category=blog.addcategory.lower()
        categorie_=Categories.objects.all()
        categories_=[]
        for cat in categorie_:
            categories_.append(cat.name)
        print(categories_)
        if blog.addcategory:
            if category!='none':
                if category not in categories_:
                    categories=Categories.objects.create(
                        name=blog.addcategory,
                    )
        
post_save.connect(updateTag, sender= Blog)
post_save.connect(updateCategory, sender= Blog)