from django.db import models
from datetime import datetime

class Product(models.Model):
    product_id = models.CharField(max_length=16, primary_key=True),
    product_name = models.CharField(max_length=16)
    product_label = models.CharField(max_length=16)
    product_type = models.CharField(max_length=16)
    product_description = models.CharField(max_length=16)
    product_price = models.CharField(max_length=16)
    product_image = models.ImageField()
    product_offer = models.CharField(max_length=16)
    product_added = models.DateTimeField(default=datetime.now)
    product_exist = models.BooleanField(default=True)
