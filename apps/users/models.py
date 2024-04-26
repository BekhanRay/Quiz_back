from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    email = models
    username = models.CharField(max_length=124, unique=True)
    is_staff = models.BooleanField(default=False)