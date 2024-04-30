from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from apps.users.management.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=124, unique=True)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', ]

    objects = UserManager()

    def __str__(self):
        return self.username

    def is_superuser(self):
        return self.is_staff
