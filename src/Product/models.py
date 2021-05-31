from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=210)
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/',default='no_picture.png')


