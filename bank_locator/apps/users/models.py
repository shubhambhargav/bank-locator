"""User models"""
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class CustomUserModel(AbstractBaseUser):
    """Custom user definition for consumption"""
    name = models.CharField(blank=True, max_length=255)
