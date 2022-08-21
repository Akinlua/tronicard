from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User

from .models import Profile
from django.core.mail import send_mail
from django.conf import settings

def createProfile(sender, instance, created, **kwargs ):
    if created:
        user= instance
        profile = Profile.objects.create(
            user= user,
            username= user.username,
            email = user.email,
            name= user.first_name,
        )
        subject= "Welcome" 
        message= "We kindly welcome you to Tronicard community, where the word of God is being preached."

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )
        

def deleteUser(sender, instance, **kwargs):
    user= instance.user
    user.delete()


post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)