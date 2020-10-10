from django.test import TestCase
from app.calc import add

class ClacTests(TestCase):
  def test_add_numbers(self):
    """Test if the value are added together"""
    self.assertEqual(add(3, 8), 11)