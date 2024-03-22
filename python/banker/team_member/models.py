from django.db import models

# Create your models here.


class TeamMemberModel(models.Model):
    id=models.BigIntegerField(primary_key=True)
    name=models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    image=models.TextField(blank=True)
    facebook_url = models.CharField(max_length=255)
    twitter_url = models.CharField(max_length=255)
    linkedin_url = models.CharField(max_length=255)
    instagram_url = models.CharField(max_length=255)
