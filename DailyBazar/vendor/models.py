from django.db import models
from datetime import datetime

class Vendor(models.Model):
    vendor_id = models.CharField(max_length=16, primary_key=True)
    vendor_name = models.CharField(max_length=64)
    vendor_email = models.CharField(max_length=64)
    vendor_password = models.CharField(max_length=64)
    vendor_phone = models.CharField(max_length=16)
    vendor_city = models.CharField(max_length=64)
    vendor_state = models.CharField(max_length=64)
    vendor_country = models.CharField(max_length=64)
    vendor_longitude = models.CharField(max_length=128)
    vendor_latitude = models.CharField(max_length=128)
    vendor_joined = models.DateTimeField(default=datetime.now)
    vendor_exist = models.BooleanField(default=True)
