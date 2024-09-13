# Generated by Django 5.1.1 on 2024-09-13 10:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyClubUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Venue Name')),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10, verbose_name='Phone Number')),
                ('zip_code', models.CharField(blank=True, max_length=10, verbose_name='Zip Code')),
                ('web', models.URLField(blank=True, verbose_name='Website address')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('owner', models.IntegerField(default=1, verbose_name='Venue Owner')),
                ('venue_image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Event Name')),
                ('event_date', models.DateTimeField(verbose_name='Event Date')),
                ('description', models.TextField(blank=True)),
                ('approved', models.BooleanField(default=False, verbose_name='Approved')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('attendees', models.ManyToManyField(blank=True, to='events.myclubuser')),
                ('venue', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='events.venue')),
            ],
        ),
    ]
