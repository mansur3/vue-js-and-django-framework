from django.db import models

# Create your models here.

class OurServicesModel(models.Model):
    id=models.BigIntegerField(primary_key=True)
    icon=models.CharField(max_length=255)
    title=models.CharField(max_length=255)
    description=models.TextField()
    cta_button_title = models.CharField(max_length=255)
    cta_button_url = models.CharField(max_length=255)


