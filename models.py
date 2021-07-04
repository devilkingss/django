from django.db import models
# Create your models here.
class details(models.Model):
    productname = models.TextField()
    name = models.TextField()
    address = models.TextField()
    phonenumber = models.IntegerField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    offer = models.BooleanField(default=False)