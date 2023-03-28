from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Image(models.Model):
    user_id = models.IntegerField(null=False)
    image_id = models.CharField(max_length=35, null=True)
    image_class = models.CharField(max_length=10, null=True)


class Model(models.Model):
    name = models.CharField(max_length=80, null=True)
