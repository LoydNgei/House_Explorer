from django.db import models
import uuid

class houses(models.Model):
    """Class for the houses to be displayed on the website"""
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    img = models.ImageField(upload_to='House/files/pics')
    desc = models.TextField()
    is_featured = models.BooleanField(default=False)