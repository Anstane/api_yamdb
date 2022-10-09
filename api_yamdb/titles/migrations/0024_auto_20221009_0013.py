# Generated by Django 2.2.16 on 2022-10-08 21:13

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0023_auto_20221009_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.IntegerField(blank=True, default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.UUIDField(default=uuid.UUID('12eac9b8-6668-4f5b-9ec9-69388e8240a9'), editable=False),
        ),
    ]