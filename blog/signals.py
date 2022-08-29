from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User

from .models import Tags, Blog, Categories

from users.models import Profile
from django.core.mail import send_mail
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


def sendNotifications(sender, instance, created, **kwargs):
    if created:
        print('send')
        blog=instance
        html_content=(               
                    '\
                    Click the following link to read the new post: {}- https://tronicard.herokuapp.com/single-blog/{}/ \
                    '\
                    ).format(
                    blog.title,
                    blog.id,
                    )
        subject= "New Blog Post" 
        message= "Kindly check out our new post Blog. "
        emails = Profile.objects.values_list('email', flat=True) 
        mass_emails=[] 
        for i in emails: 
            mass_emails.append(i)
        sender_ = blog.owner.email
        mass_emails.remove(sender_)
        send_mail(
            subject,
            html_content,
            settings.EMAIL_HOST_USER,
            mass_emails,
            fail_silently=False,
        )

post_save.connect(updateTag, sender= Blog)
post_save.connect(updateCategory, sender= Blog)
post_save.connect(sendNotifications, sender=Blog)