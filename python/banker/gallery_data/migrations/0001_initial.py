# Generated by Django 5.0.3 on 2024-03-26 05:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryCategoryModel',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('item_title', models.CharField(max_length=255)),
                ('short_key', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GalleryModel',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('image', models.TextField(blank=True)),
                ('title', models.CharField(blank=True)),
                ('gallery_category_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery_data.gallerycategorymodel')),
            ],
        ),
    ]