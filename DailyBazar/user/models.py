from django.db import models
from datetime import datetime

class User(models.Model):
    user_id = models.CharField(max_length=16, primary_key=True)
    user_name = models.CharField(max_length=64)
    user_email = models.CharField(max_length=64)
    user_phone = models.CharField(max_length=16)
    user_password = models.CharField(max_length=16)
    user_joined = models.DateTimeField(default=datetime.now)
    user_exist = models.BooleanField(default=True)

