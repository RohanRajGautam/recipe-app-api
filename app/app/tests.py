from django.test import TestCase
from app.calc import add, subtract

class ClacTests(TestCase):
  def test_add_numbers(self):
    """Test if the value are added together"""
    self.assertEqual(add(3, 8), 11)

  def test_subtract_numbers(self):
    """Test if the value are subtrated together"""
    self.assertEqual(subtract(5, 11), 6)