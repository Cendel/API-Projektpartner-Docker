from django.db import models
from django_use_email_as_username.models import BaseUser, BaseUserManager


# Create your models here.


class User(BaseUser):
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255, default="", blank=True, null=True)
    location = models.CharField(max_length=255, default="", blank=True, null=True)
    about = models.TextField(blank=True, default="", null=True)
    phone = models.CharField(max_length=20, default="", blank=True, null=True)
    website = models.CharField(max_length=255, default="", blank=True, null=True)
    confirmPassword = models.CharField(max_length=30, blank=True, null=True)

    objects = BaseUserManager()
