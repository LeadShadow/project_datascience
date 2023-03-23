from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Files(models.Model):
    user_id = models.IntegerField(null=False)
    file = models.FileField(null=True)
    up_time = models.DateTimeField(default=datetime.now())


class Model(models.Model):
    name = models.CharField(max_length=80, null=True)
