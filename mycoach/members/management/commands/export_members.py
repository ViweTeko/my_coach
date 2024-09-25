"""This script exports members (athletes) data to CSV file"""
from django.core.management.base import BaseCommand
from members.models import Member
import csv

class Command(BaseCommand):
    help = 'Exports member data to a CSV file.'

    def handle(self, *args, **options):
        with open('members.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(
            [
                'id',
                'name',
                'surname',
                'gender',
                'age',
                'club',
                'athlete_event',
                'athlete_image',
            ])

            for member in Member.objects.all():
                writer.writerow(
                [
                    member.id,
                    member.name,
                    member.surname,
                    member.gender,
                    member.age,
                    member.club,
                    member.athlete_event,
                    member.athlete_image,
                ])
        self.stdout.write(
        self.style.SUCCESS('Member data exported to members.csv'))
