

from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from .models import *




@receiver(post_save,sender=User)
def create_wishlist(sender,instance,created,**kwargs):
    if created:
        Wishlist.objects.create(user=instance) 



@receiver(post_save,sender=User)
def create_history(sender,instance,created,**kwargs):
    if created:
        BrowsingHistory.objects.create(user=instance)