# Generated by Django 5.0.3 on 2024-03-20 09:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicemodel',
            name='items',
        ),
        migrations.AddField(
            model_name='descriptionitemmodel',
            name='service',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='service.servicemodel'),
            preserve_default=False,
        ),
    ]