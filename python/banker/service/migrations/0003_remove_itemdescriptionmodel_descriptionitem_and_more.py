# Generated by Django 5.0.3 on 2024-03-20 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_remove_servicemodel_items_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemdescriptionmodel',
            name='descriptionItem',
        ),
        migrations.RemoveField(
            model_name='itemdescriptionmodel',
            name='service',
        ),
        migrations.AlterField(
            model_name='serviceitem',
            name='icon',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='servicemodel',
            name='image',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='DescriptionItemModel',
        ),
        migrations.DeleteModel(
            name='ItemDescriptionModel',
        ),
    ]
