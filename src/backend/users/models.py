from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    '''Custom User model extending the base user model'''
    birth_date = models.DateField(null=True, blank=True)
