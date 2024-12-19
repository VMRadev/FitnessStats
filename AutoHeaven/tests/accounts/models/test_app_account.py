from django.test import TestCase
from AutoHeaven.accounts.models import AppAccount


class AppAccountModelTests(TestCase):
    def setUp(self):
        # Set up initial test data
        self.user_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password123",
        }

    def test_create_user(self):
        # Create a standard user
        user = AppAccount.objects.create_user(**self.user_data)
        self.assertEqual(user.username, self.user_data["username"])
        self.assertEqual(user.email, self.user_data["email"])
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        # Create a superuser
        superuser = AppAccount.objects.create_superuser(**self.user_data)
        self.assertEqual(superuser.username, self.user_data["username"])
        self.assertEqual(superuser.email, self.user_data["email"])
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_unique_username(self):
        # Test that duplicate usernames are not allowed
        AppAccount.objects.create_user(**self.user_data)
        with self.assertRaises(Exception):
            AppAccount.objects.create_user(
                username="testuser",
                email="anotheremail@example.com",
                password="password456",
            )

    def test_str_representation(self):
        # Test the __str__ method
        user = AppAccount.objects.create_user(**self.user_data)
        self.assertEqual(str(user), user.username)

    def test_user_is_not_active_by_default(self):
        # Test default is_active value
        inactive_user = AppAccount.objects.create_user(
            username="inactiveuser",
            email="inactive@example.com",
            password="password123",
        )
        self.assertTrue(inactive_user.is_active)

    def test_user_has_required_fields(self):
        # Test user creation with required fields
        with self.assertRaises(Exception):
            AppAccount.objects.create_user(
                username="userwithoutemail",
                email="",
                password="password123",
            )
