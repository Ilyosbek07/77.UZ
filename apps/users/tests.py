from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse


class UserTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )

    def test_user_creation(self):
        user = self.user
        self.assertTrue(isinstance(user, get_user_model()))
        self.assertEqual(user.str(), user.email)

    # def test_user_login(self):
    #     response = self.client.login(username='testuser', password='testpassword')
    #     self.assertTrue(response)
    #     response = self.client.get(reverse('user-profile'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'test@example.com')
#