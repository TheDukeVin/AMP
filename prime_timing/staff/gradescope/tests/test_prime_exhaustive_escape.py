import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from prime_timing import is_prime_exhaustive_escape

class TestEx1(unittest.TestCase):
  @weight(1)
  @number("2.1")
  def test_1(self):
      """is_prime_exhaustive_escape: Single Even Composite Number"""
      prime = is_prime_exhaustive_escape(12)
      self.assertEqual(prime, False)

  @weight(1)
  @number("2.2")
  def test_2(self):
      """is_prime_exhaustive_escape: Single Odd Prime Number"""
      prime = is_prime_exhaustive_escape(17)
      self.assertEqual(prime, True)

  @weight(1)
  @number("2.3")
  def test_3(self):
      """is_prime_exhaustive_escape: Single Even Prime Number"""
      prime = is_prime_exhaustive_escape(2)
      self.assertEqual(prime, True)

  @weight(1)
  @number("2.4")
  def test_4(self):
      """is_prime_exhaustive_escape: Single Odd Composite Number"""
      prime = is_prime_exhaustive_escape(35)
      self.assertEqual(prime, False)

  @weight(1)
  @number("2.5")
  def test_5(self):
     """is_prime_exhaustive_escape: 0"""
     prime = is_prime_exhaustive_escape(0)
     self.assertEqual(prime, False)

  @weight(1)
  @number("2.6")
  def test_6(self):
        """is_prime_exhaustive_escape: 1"""
        prime = is_prime_exhaustive_escape(1)
        self.assertEqual(prime, False)

  @weight(1)
  @number("2.7")
  def test_7(self):
        """is_prime_exhaustive_escape: All primes less than 100"""
        actualPrimes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        testPrimes=[]
        for n in range(1, 101):
            if is_prime_exhaustive_escape(n):
                testPrimes.append(n)
        prime = is_prime_exhaustive_escape(-17)
        self.assertEqual(testPrimes, actualPrimes)

  @weight(1)
  @number("2.8")
  def test_8(self):
        """is_prime_exhaustive_escape: Negative Number"""
        prime = is_prime_exhaustive_escape(-35)
        self.assertEqual(prime, False)