from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)

class UserAddress(models.Model):
    user = models.ForeignKey(User, related_name="userad", on_delete=models.CASCADE, blank=True, null=True)
    country = models.CharField(max_length=255, default="Nederland", blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=7, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    house_number = models.CharField(max_length=255, blank=True, null=True)

class BillingAddress(models.Model):
    user = models.ForeignKey(User, related_name="userbil", on_delete=models.CASCADE, blank=True, null=True)
    country = models.CharField(max_length=255, default="Nederland", blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=7, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    house_number = models.CharField(max_length=255, blank=True, null=True)
