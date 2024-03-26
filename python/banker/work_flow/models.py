from django.db import models

# Create your models here.
class WorkFlowItemModel(models.Model):
    id = models.BigIntegerField(primary_key=True)
    image=models.TextField(blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    cta_button_title = models.TextField(blank=True)
    cta_button_url = models.TextField(blank=True)


class WorkFlowModel(models.Model):
    id = models.BigIntegerField(primary_key=True)
    header_title = models.TextField(blank=True)
    header_description = models.TextField(blank=True)
    work_flow_item_id = models.ForeignKey(WorkFlowItemModel, on_delete=models.CASCADE)
