from django.test import TestCase
from AutoHeaven.accounts.models import AppAccount, Profile
from AutoHeaven.cars.choices import CarTransmissionType


class ProfileModelTests(TestCase):
    def setUp(self):
        # Set up a test user
        self.user = AppAccount.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="password123",
        )

    def test_profile_creation(self):
        # Test if profile is created correctly
        profile = Profile.objects.get(user=self.user)
        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.first_name, None)
        self.assertEqual(profile.last_name, None)
        self.assertEqual(profile.age, None)
        self.assertEqual(profile.height, 0)  # Default value
        self.assertEqual(profile.description, None)
        self.assertEqual(profile.preferred_transmission, None)

    def test_str_representation_with_name(self):
        # Test __str__ with first and last name
        profile = Profile.objects.get(user=self.user)
        profile.first_name = "John"
        profile.last_name = "Doe"
        profile.save()
        self.assertEqual(str(profile), "John Doe")

    def test_str_representation_without_name(self):
        # Test __str__ without first and last name
        profile = Profile.objects.get(user=self.user)
        self.assertEqual(str(profile), "testuser")

    def test_blank_and_null_fields(self):
        # Test a profile with all blank and null fields
        another_user = AppAccount.objects.create_user(
            username="anotheruser",
            email="anotheruser@example.com",
            password="password123",
        )
        profile = Profile.objects.get(user=another_user)
        self.assertIsNone(profile.first_name)
        self.assertIsNone(profile.last_name)
        self.assertIsNone(profile.age)
        self.assertEqual(profile.height, 0)  # Default value
        self.assertIsNone(profile.description)
        self.assertIsNone(profile.preferred_transmission)

    def test_cloudinary_field(self):
        # Test CloudinaryField for the image
        profile = Profile.objects.get(user=self.user)
        profile.image = "test_image.jpg"
        profile.save()
        self.assertEqual(profile.image, "test_image.jpg")

    def test_related_name(self):
        # Test related_name "profile" on the user model
        profile = self.user.profile
        self.assertEqual(profile.user, self.user)

    def test_update_profile_fields(self):
        # Test updating profile fields
        profile = Profile.objects.get(user=self.user)
        profile.first_name = "Jane"
        profile.last_name = "Doe"
        profile.age = 25
        profile.height = 165
        profile.description = "Loves driving sports cars."
        profile.preferred_transmission = CarTransmissionType.AUTOMATIC
        profile.save()

        updated_profile = Profile.objects.get(user=self.user)
        self.assertEqual(updated_profile.first_name, "Jane")
        self.assertEqual(updated_profile.last_name, "Doe")
        self.assertEqual(updated_profile.age, 25)
        self.assertEqual(updated_profile.height, 165)
        self.assertEqual(updated_profile.description, "Loves driving sports cars.")
        self.assertEqual(updated_profile.preferred_transmission, CarTransmissionType.AUTOMATIC)
