# Generated by Django 2.2.16 on 2022-10-09 13:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0030_auto_20221009_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.UUIDField(default=uuid.UUID('6484d0e9-c853-4197-87e9-06b85e1cdd4f'), editable=False),
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('author', 'title'), name='unique_author_title'),
        ),
    ]
