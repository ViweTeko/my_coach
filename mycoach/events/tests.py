from django.test import TestCase
from .models import Venue, Event
from .forms import VenueForm

class TestVenueModel(TestCase):
    """Test Venue Model."""

    def setUp(self):
        """Set up for test."""
        self.venue = Venue.objects.create(
            name = 'Venue 1',
            address = 'Address 1',
            zip_code = '12345',
            phone = '1234567890',
            web = 'www.venue1.com',
            email_address = 'venue1@email.com'
        )    

    def test_venue_model_str(self):
        """Test venue model str."""
        self.assertEqual(str(self.venue), 'Venue 1')

class TestEventModel(TestCase):
    """Test Event Model."""

    def setUp(self):
        """Set up for test."""
        self.venue = Venue.objects.create(
            name = 'Venue 1',
            address = 'Address 1',
            zip_code = '12345',
            phone = '1234567890',
            web = 'www.venue1.com',
            email_address = 'venue1@email.com'
        )
        self.event = Event.objects.create(
            name = 'Event 1',
            event_date = '2024-01-01',
            venue = self.venue,
            manager = 'Manager 1',
            attendees = 10,
            description = 'Description 1'
        )

    def test_event_model_str(self):
        """Test event model str."""
        self.assertEqual(str(self.event), 'Event 1')



class TestVenueForm(TestCase):
    """Test Venue Form."""
    def test_venue_name_is_required(self):
        form = VenueForm({'name':''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_venue_name_is_less_than_120_chars(self):
        form = VenueForm({'name':'a'*121})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'Ensure this value has at most 120 characters (it has 121).')

    def test_venue_email_is_optional(self):
        form = VenueForm({'email':''})
        self.assertTrue(form.is_valid())

    def test_venue_email_is_less_than_254_chars(self):
        form = VenueForm({'email':'a'*255})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'Ensure this value has at most 254 characters (it has 255).')

    def test_venue_phone_is_optional(self):
        form = VenueForm({'phone':''})
        self.assertTrue(form.is_valid())

    def test_venue_address_is_required(self):
        form = VenueForm({'address':''})
        self.assertFalse(form.is_valid())
        self.assertIn('address', form.errors.keys())
        self.assertEqual(form.errors['address'][0], 'This field is required.')

    def test_venue_address_is_less_than_255_chars(self):
        form = VenueForm({'address':'a'*256})
        self.assertFalse(form.is_valid())
        self.assertIn('address', form.errors.keys())
        self.assertEqual(form.errors['address'][0], 'Ensure this value has at most 255 characters (it has 256).')

    def test_venue_zip_code_is_required(self):
        form = VenueForm({'zip_code':''})
        self.assertFalse(form.is_valid())
        self.assertIn('zip_code', form.errors.keys())
        self.assertEqual(form.errors['zip_code'][0], 'This field is required.')

    def test_venue_zip_code_is_less_than_10_chars(self):
        form = VenueForm({'zip_code':'a'*11})
        self.assertFalse(form.is_valid())
        self.assertIn('zip_code', form.errors.keys())
        self.assertEqual(form.errors['zip_code'][0], 'Ensure this value has at most 10 characters (it has 11).')

    def test_venue_web_is_optional(self):
        form = VenueForm({'web':''})
        self.assertTrue(form.is_valid())

    def test_venue_web_is_less_than_50_chars(self):
        form = VenueForm({'web':'a'*51})
        self.assertFalse(form.is_valid())
        self.assertIn('web', form.errors.keys())
        self.assertEqual(form.errors['web'][0], 'Ensure this value has at most 50 characters (it has 51).')

    def test_venue_description_is_optional(self):
        form = VenueForm({'description':''})
        self.assertTrue(form.is_valid())
