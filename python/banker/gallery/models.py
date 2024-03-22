from django.db import models

# Create your models here.

class GalleryModel(models.Model):
    id = models.BigIntegerField(primary_key=True)
    image=models.TextField(blank=True)
    title=models.CharField(blank=True)

class GalleryCategoryModel(models.Model):
    id = models.BigIntegerField(primary_key=True)
    gallery_item_id = models.ForeignKey(GalleryModel, on_delete=models.CASCADE)
    item=models.CharField(max_length=255)
    short_key = models.CharField(max_length=255)

