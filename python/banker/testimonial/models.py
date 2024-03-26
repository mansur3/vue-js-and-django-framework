from django.db import models

# Create your models here.

class TestimonialModel(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    