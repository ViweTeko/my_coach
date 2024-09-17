from django.test import TestCase
from django.contrib.auth.models import User
from .models import Member

class MemberViewsTest(TestCase):
    def test_login_view(self):
        response = self.client.get('/members/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authenticate/login.html')

    def test_register_user_view(self):
        response = self.client.get('/members/register_user/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authenticate/register_user.html')

    def test_register_user_with_valid_data(self):
        response = self.client.post('/members/register_user/', {'username': 'testuser', 'first_name': 'Test', 'last_name': 'User', 'email': 'test@example.com', 'password': 'testpassword', 'password2': 'testpassword'})
        self.assertRedirects(response, '/members/login/')
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(Member.objects.count(), 1)

    def test_register_user_with_invalid_data(self):
        response = self.client.post('/members/register_user/', {'username': 'testuser', 'first_name': 'Test', 'last_name': 'User', 'email': 'test@example.com', 'password': 'testpassword', 'password2': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authenticate/register_user.html')
        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(Member.objects.count(), 0)

    def test_login_with_valid_data(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        Member.objects.create(user=user)
        response = self.client.post('/members/login/', {'username': 'testuser', 'password': 'testpassword'})
        self.assertRedirects(response, '/')
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_with_invalid_data(self):
        response = self.client.post('/members/login/', {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authenticate/login.html')
        self.assertFalse(response.wsgi_request.user.is_authenticated)