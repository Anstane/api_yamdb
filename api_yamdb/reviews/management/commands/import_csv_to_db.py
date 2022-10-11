import csv

from django.core.management.base import BaseCommand, CommandError

from reviews.models import (
    User,
    Category,
    Genre,
    Title,
    Review,
    Comment,
)


""" 
    class Command(BaseCommand):
    help = 'Import data from .csv files to the database.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs='+', type=str)

    def handle(self, *args, **options):
        for csv_file in options['csv_file']:
            dataReader = csv.reader(open(csv_file), delimiter=',', quotechar='"')
 """