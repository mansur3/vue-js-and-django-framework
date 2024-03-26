from django.db import models

# Create your models here.

class UserModel(models.Model):
    id=models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email=models.EmailField(blank=True)
    is_active = models.BooleanField(default=True)
