from django.db import models

# Create your models here.

class BannerModel(models.Model):
    banner_name = models.CharField(max_length=255)
    banner_title = models.CharField(max_length=255)
    banner_description = models.TextField(max_length=255)
    banner_image = models.TextField(max_length=1000)
    
