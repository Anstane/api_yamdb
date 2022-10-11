from django.core.management.base import BaseCommand

from reviews import models

from . import _common

class Command(BaseCommand):

    def handle(self, *args, **options):

        _common.create_items(
            'static/data/category.csv',
            models.Category.objects,
        )

        # _common.create_items(
        #     'static/data/users.csv',
        #     models.Category.objects,
        # )
