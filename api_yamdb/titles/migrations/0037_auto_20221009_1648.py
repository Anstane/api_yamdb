# Generated by Django 2.2.16 on 2022-10-09 13:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0036_auto_20221009_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.UUIDField(default=uuid.UUID('f2a9c650-f8d1-466c-af68-249c7cb26bae'), editable=False),
        ),
    ]
