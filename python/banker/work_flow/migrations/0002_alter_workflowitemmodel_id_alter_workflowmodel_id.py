# Generated by Django 5.0.3 on 2024-03-26 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_flow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workflowitemmodel',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='workflowmodel',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]