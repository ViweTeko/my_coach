"""This script imports members (athletes) from a CSV file."""
from django.core.management.base import BaseCommand
from members.models import Member
import csv

class Command(BaseCommand):
    help = 'Imports member data from a CSV file.'

    def handle(self, *args, **options):
        with open('members.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skips the header row

            for row in reader:
                Member.objects.create(
                    id=row[0],
                    name=row[1],
                    surname=row[2],
                    gender=row[3],
                    age=row[4],
                    club=row[5],
                    athlete_event=row[6],
                    athlete_image=row[7],
                )
        self.stdout.write(
        self.style.SUCCESS('Member data imported successfully.'))
