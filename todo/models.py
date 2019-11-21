# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
from django.db import models
import datetime


class Category(models.Model):
    title = models.CharField(max_length=100)


class Note(models.Model):
    created = models.DateTimeField(default=datetime.datetime.now)
    user = models.CharField(max_length=50)
    text = models.CharField(max_length=500)
    color = models.CharField(max_length=10)
    # category = models.ForeignKey(
    #     Category,
    #     models.CASCADE
    # )

    def __str__(self):
        return self.text
    
