from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='rohan@rrg.com.np', password='testpass'):
  """Create a sample user"""
  return get_user_model().objects.create_user(email, password)

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


  def test_new_user_invalid_email(self):
    """Test creating user with no email raises error"""
    with self.assertRaises(ValueError):
      get_user_model().objects.create_user(None, 'test123')

  
  def test_create_new_superuser(self):
    """Test creating a new superuser"""
    user = get_user_model().objects.create_superuser(
      'rohan@rrg.com.np',
      'test123'
    )

    self.assertTrue(user.is_superuser)
    self.assertTrue(user.is_staff)

  def test_tag_str(self):
    """TEst the tag string representation"""
    tag = models.Tag.objects.create(
        user=sample_user(),
        name='Vegan'
    )

    self.assertEqual(str(tag), tag.name)

  def test_ingredint_str(self):
    """Test the ingredent string representation"""
    ingredient = models.Ingredient.objects.create(
        user=sample_user(),
        name='Cucumber'
    )
    
    self.assertEqual(str(ingredient), ingredient.name)

  def test_recipe_str(self):
     """Test the recipe string representation"""
     recipe = models.Recipe.objects.create(
         user=sample_user(),
         title='Streak and mushroom sause',
         time_minutes=5,
         price=5.00
     )
