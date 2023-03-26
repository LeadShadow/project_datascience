from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Image(models.Model):
    user_id = models.IntegerField(null=False)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    image_id = models.IntegerField(null=False)
    up_time = models.DateTimeField(default=datetime.now())


class Model(models.Model):
    name = models.CharField(max_length=80, null=True)
