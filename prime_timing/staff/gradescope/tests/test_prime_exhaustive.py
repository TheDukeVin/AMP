import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from prime_timing import is_prime_exhaustive

class TestEx1(unittest.TestCase):
  @weight(1)
  @number("1.1")
  def test_1(self):
      """is_prime_exhaustive: Single Even Composite Number"""
      prime = is_prime_exhaustive(12)
      self.assertEqual(prime, False)

  @weight(1)
  @number("1.2")
  def test_2(self):
      """is_prime_exhaustive: Single Odd Prime Number"""
      prime = is_prime_exhaustive(17)
      self.assertEqual(prime, True)

  @weight(1)
  @number("1.3")
  def test_3(self):
      """is_prime_exhaustive: Single Even Prime Number"""
      prime = is_prime_exhaustive(2)
      self.assertEqual(prime, True)

  @weight(1)
  @number("1.4")
  def test_4(self):
      """is_prime_exhaustive: Single Odd Composite Number"""
      prime = is_prime_exhaustive(35)
      self.assertEqual(prime, False)

  @weight(1)
  @number("1.5")
  def test_5(self):
     """is_prime_exhaustive: 0"""
     prime = is_prime_exhaustive(0)
     self.assertEqual(prime, False)

  @weight(1)
  @number("1.6")
  def test_6(self):
        """is_prime_exhaustive: 1"""
        prime = is_prime_exhaustive(1)
        self.assertEqual(prime, False)

  @weight(1)
  @number("1.7")
  def test_7(self):
        """is_prime_exhaustive: All primes less than 100"""
        actualPrimes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        testPrimes=[]
        for n in range(1, 101):
            if is_prime_exhaustive(n):
                testPrimes.append(n)
        prime = is_prime_exhaustive(-17)
        self.assertEqual(testPrimes, actualPrimes)

  @weight(1)
  @number("1.8")
  def test_8(self):
        """is_prime_exhaustive: Negative Number"""
        prime = is_prime_exhaustive(-35)
        self.assertEqual(prime, False)