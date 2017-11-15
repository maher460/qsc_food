# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


###########################
# USER AND PROFILE

class Profile(models.Model):

    #gender types
    UNKNOWN_TYPE = 'U'
    MALE_TYPE = 'M'
    FEMALE_TYPE = 'F'

    GENDER_TYPE_OPTIONS = (
        (UNKNOWN_TYPE, 'Unknown'),
        (MALE_TYPE, 'Male'),
        (FEMALE_TYPE, 'Female'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=1, choices=GENDER_TYPE_OPTIONS, 
                                      default=UNKNOWN_TYPE)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



# FOOD DATABASE

class Cuisine(models.Model):
    name = models.CharField(max_length=128)

class Food(models.Model):
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

class Plate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Portion(models.Model):
    plate = models.ForeignKey(Plate, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.PROTECT)


