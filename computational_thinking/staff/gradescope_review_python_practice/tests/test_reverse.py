import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from review_python_practice import reverse

class TestEx1(unittest.TestCase):
  @weight(1)
  @number("5.1")
  def test_janestreet(self):
      """reverse -  String with spaces"""
      val = reverse("Jane Street")
      self.assertEqual(val, "teertS enaJ")

  @weight(1)
  @number("5.2")
  def test_amp2023(self):
      """reverse -  String with numbers"""
      val = reverse("AMP2023")
      self.assertEqual(val, "3202PMA")

  @weight(1)
  @number("5.3")
  def test_onechar(self):
      """reverse -  Single character"""
      val = reverse("2")
      self.assertEqual(val, "2")

  @weight(1)
  @number("5.4")
  def test_zerochars(self):
      """reverse -  Zero characters"""
      val = reverse("")
      self.assertEqual(val, "")

  @weight(1)
  @number("5.5")
  def test_specialchar(self):
      """reverse -  Special characters"""
      val = reverse("3+2=5")
      self.assertEqual(val, "5=2+3")




