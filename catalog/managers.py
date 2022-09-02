
from django.db import models




class PartsManager(models.Manager):


    #  modify existing method called ; get_queryset method to ignore archived parts.
    def get_query_set(self):
        return super().get_queryset.filter(archived=False)
    # result of call all(), because  all() calls this method



    # adding a custom model manager method
    def expensive_parts(self):
        """ list of all expensive  parts"""
        return self.get_queryset.filter(price__gt=1000)
