# Generated by Django 2.2.16 on 2022-10-08 11:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0016_auto_20221008_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.UUIDField(default=uuid.UUID('58c90922-0ee4-4ddb-83a6-a4a51d2abc27'), editable=False),
        ),
    ]