from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True)
    number = models.CharField(max_length=127, null=True, blank=True)

    # def __str__(self):
    #     return f'{self.username} -- {self.number}'

