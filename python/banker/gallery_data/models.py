from django.db import models

# Create your models here.


class GalleryCategoryModel(models.Model):
    id = models.BigIntegerField(primary_key=True)
    item_title=models.CharField(max_length=255)
    short_key = models.CharField(max_length=255)

class GalleryModel(models.Model):
    id = models.BigIntegerField(primary_key=True)
    image=models.TextField(blank=True)
    title=models.CharField(blank=True)
    gallery_category_item_id = models.ForeignKey(GalleryCategoryModel, on_delete=models.CASCADE)
