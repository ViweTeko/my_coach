from django.db import models

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=100)
    surname = models.CharField('Surname', max_length=100)
    gender = models.CharField('Gender', max_length=10)
    age = models.IntegerField('Age')
    club = models.CharField('Club', max_length=100)
    athlete_event = models.CharField('Athlete Event', max_length=60)
    athlete_image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.name

