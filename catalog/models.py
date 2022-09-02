from unittest.util import _MAX_LENGTH
from django.db import models


from . managers import *
# Create your models here.





class Supplier(models.Model):
    name =  models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Part(models.Model):
    partnumber = models.CharField('unique carpart number',primary_key=True,max_length=20,help_text='unique carpart number')
    description=  models.CharField(max_length=200)
    supplier = models.ForeignKey('Supplier', on_delete=models.SET_DEFAULT,default='Missing')
    archived =models.BigIntegerField()
    status =  models.CharField(max_length=200)
    price = models.IntegerField()
    parts= PartsManager()   # custom model manager
    object = models.Manager()

    def international_supplier(self): # model method.  Row-level functionality
        return self.supplier.country != 'UK' or 'GB' or 'United Kingdom'


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