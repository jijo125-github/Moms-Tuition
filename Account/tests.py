from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

# Create your tests here.
User = get_user_model()

class UserTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username = '52118791', password = 'Jijo@123')

    def test_user_created(self):
        username = self.user.username
        self.assertEqual(username, '52118791')

    def test_login(self):
        client = APIClient()
        client.login(username = self.user.username, password = 'Jijo@123')
    
    def test_logout(self):
        client = APIClient()
        client.login(username = self.user.username, password = 'Jijo@123')
        client.logout()




