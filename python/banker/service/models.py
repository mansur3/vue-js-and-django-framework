from django.db import models

# Create your models here.
class ServiceModel(models.Model):
    page_name = models.CharField(max_length=255)
    image=models.TextField()
    title=models.CharField(max_length=255)
    description=models.TextField()
    


class ServiceItem(models.Model):
    icon=models.TextField()
    title=models.CharField(max_length=500)
    description=models.TextField()
    service=models.ForeignKey(ServiceModel, on_delete=models.CASCADE)

