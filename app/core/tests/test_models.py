from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
  def test_create_user_with_email_successful(self):
    """Test creating a new user with an email is successful"""
    email = 'rohan@rrg.com.np'
    password = 'Password123'
    user = get_user_model().objects.create_user(
      email=email,
      password=password
    )

    self.assertEqual(user.email, email)
    self.assertTrue(user.check_password(password))

  def test_new_user_email_normalizerd(self):
    """Test the email for a new user is normalized"""
    email = 'rohan@RRG.COM.NP'
    user = get_user_model().objects.create_user(email, 'test123')

    self.assertEqual(user.email, email.lower())