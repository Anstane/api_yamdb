# Generated by Django 2.2.16 on 2022-10-08 11:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0015_auto_20221008_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.UUIDField(default=uuid.UUID('5bf564ad-4560-481f-8536-02cca161f301'), editable=False),
        ),
    ]