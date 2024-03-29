from email.policy import default
from unittest.util import _MAX_LENGTH
import uuid
from django.urls import reverse
from django.db import models
from django.template.defaultfilters import slugify

from user.models import CustomUser
from . managers import *
# Create your models here.


class Supplier(models.Model):
    name =  models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    email = models.EmailField()
 
    
    def get_absolute_url(self):
        return reverse('api:supplierdetail',args=[self.id])

    def __str__(self):
        return self.name


class Part(models.Model):
    partnumber = models.CharField('unique carpart number',primary_key=True,max_length=20,help_text='unique carpart number')
    
    description=  models.CharField(max_length=200)
    supplier = models.ForeignKey('Supplier', related_name='parts', on_delete=models.SET_DEFAULT,default=1)
    archived =models.BooleanField(null=True)
    status =  models.CharField(max_length=200,null=True)
    image= models.ImageField(null=True,upload_to="images",default="images/default.jpg")
    specification = models.FileField(null=True,upload_to="documents")
    price = models.IntegerField(null=True)
    parts= PartsManager()   # custom model manager
  
    objects = models.Manager()

    def international_supplier(self): # model method.  Row-level functionality
        origin=  ['UK','GB','United Kingdom']
        return self.supplier.country not in origin
    
    def get_absolute_url(self):
        return reverse('api:partdetail',args=[self.partnumber])


    def __str__(self):
        return self.partnumber

    class Meta:
        ordering = ["partnumber"]
        verbose_name_plural = "parts"


class Carmodel(models.Model):
    manufacturers = (
        ('BMW','bmw' ),
        ('AUDI', 'audi'),
        ('LandRover','landrover' ))
    name = models.CharField(max_length=200)
    manufacturer =models.CharField(choices=manufacturers, max_length=50)
    part = models.ManyToManyField(Part)

    def __str__(self):
        return self.name