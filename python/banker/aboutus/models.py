from django.db import models

# Create your models here.

class AboutUsModel(models.Model):
    id=models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    sub_description = models.TextField(max_length=255)
    image = models.TextField()
    sub_title = models.TextField()
    description = models.TextField()

