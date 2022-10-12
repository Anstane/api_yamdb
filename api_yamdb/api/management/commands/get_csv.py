from django.core.management.base import BaseCommand

from reviews import models

from . import _common

class Command(BaseCommand):

    def handle(self, *args, **options):


        _common.create_items(
            'static/data/users.csv',
            models.Users.objects,
        )
        _common.create_items(
            'static/data/category.csv',
            models.Category.objects,
        )

        _common.create_items(
            'static/data/titles.csv',
            models.Review.objects,
        )

        _common.create_items(
            'static/data/genre.csv',
            models.Genre.objects,
        )

        _common.create_items(
            'static/data/genre_title.csv',
            models.Genre_title.objects,
        )

        _common.create_items(
            'static/data/review.csv',
            models.Review.objects,
        )
