from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import userProfile


@receiver(post_save, sender = User)
def userProfileCreation(sender, instance, created, **kwargs):

    if created:
        user = instance 
        profile = userProfile.objects.create(
            user = user, 
            username = user.username,
            email = user.email
        )

