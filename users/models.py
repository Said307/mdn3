from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.contrib.auth.base_user import BaseUserManager
from django_countries.fields import CountryField


from .managers import *

# Create your models here.


GENDER_CHOICES = (
    ("MALE", "Male"),
    ("FEMALE", "Female"),
    ("OTHER", "Other"),
)


 

       
 


class Profile(models.Model):
    """ regex=r'^(01)\d{9}$'  phone number must start with 01 followed by 9 digits"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(
        default='profile_images/default_avatar.png',
        upload_to='profile_images',
        null=True,
        blank=True
    )
    date_of_birthday = models.DateField(
        null=True,
        blank=True
    )
    gender = models.CharField(
        choices=GENDER_CHOICES,
        max_length=10,
        null=True,
        blank=True
    )

    regex_message = 'Phone number must be entered in the format: 01999999999'
    regex_validator = RegexValidator(r'^(01)\d{9}$',message=regex_message)
    phone_number = models.IntegerField(
        null=True,
        blank=True,
        validators=[regex_validator])
    objects =  CustomUserManager()




    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"



class Address(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='addresses',
        null=True
    )
    first_name = models.CharField(
        'First Name',
        max_length=79,
        null=False,
        blank=False
    )
    last_name = models.CharField(
        'Last Name',
        max_length=79,
        null=False,
        blank=False
    )

    phone_message = 'Phone number must be entered in the format: 01999999999'
    phone_regex = RegexValidator(
        regex=r'^(01)\d{9}$',
        message=phone_message
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=79,
        null=True,
        blank=True
    )

    address1 = models.CharField(
        'Address Line 1',
        max_length=255,
        null=False,
        blank=False
    )
    address2 = models.CharField(
        'Address Line 2',
        max_length=255,
        null=True,
        blank=True
    )
    zip_code = models.CharField(
        'ZIP',
        max_length=10,
        null=False,
        blank=False
    )
    city = models.CharField(
        'City',
        max_length=79,
        null=False,
        blank=False
    )
    country = CountryField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "Shipping Address"
        verbose_name_plural = "Shipping Addresses"



