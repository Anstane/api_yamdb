# Generated by Django 2.2.16 on 2022-10-09 22:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0046_auto_20221009_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.UUIDField(default=uuid.UUID('14fa1404-21fd-4339-bb7a-b78aaf4a7145'), editable=False),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set(),
        ),
    ]
