# Generated by Django 2.2.16 on 2022-10-10 14:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20221010_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.UUIDField(default=uuid.UUID('612de704-e98d-4ddf-8786-25142725ab3f'), editable=False),
        ),
    ]