from django.db import models
from django.db.models.fields import EmailField
from House.models import houses

# Create your models here.
class Contact(models.Model):
    """contact model"""
    house = models.ForeignKey(houses, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()
    contact_date = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Contact'