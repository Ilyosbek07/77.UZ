from django.contrib.auth import get_user_model
from django.test import TestCase

from apps.store.models import Category
from apps.users.models import User


class UserTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name="aaa")

        cls.user = User.objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secret",
            phone_number="+998974436638",
            category=cls.category.pk,
        )

    def test_user_model(self):
        self.assertEqual(self.user.user_name, "testuser")
        self.assertEqual(self.user.password, "secret")
        self.assertEqual(self.user.email, "test@email.com")
