import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from prime_timing import is_prime_skip_impossible_factors

class TestEx1(unittest.TestCase):
  @weight(1)
  @number("4.1")
  def test_1(self):
      """is_prime_skip_impossible_factors: Single Even Composite Number"""
      prime = is_prime_skip_impossible_factors(12)
      self.assertEqual(prime, False)

  @weight(1)
  @number("4.2")
  def test_2(self):
      """is_prime_skip_impossible_factors: Single Odd Prime Number"""
      prime = is_prime_skip_impossible_factors(17)
      self.assertEqual(prime, True)

  @weight(1)
  @number("4.3")
  def test_3(self):
      """is_prime_skip_impossible_factors: Single Even Prime Number"""
      prime = is_prime_skip_impossible_factors(2)
      self.assertEqual(prime, True)

  @weight(1)
  @number("4.4")
  def test_4(self):
      """is_prime_skip_impossible_factors: Single Odd Composite Number"""
      prime = is_prime_skip_impossible_factors(35)
      self.assertEqual(prime, False)

  @weight(1)
  @number("4.5")
  def test_5(self):
     """is_prime_skip_impossible_factors: 0"""
     prime = is_prime_skip_impossible_factors(0)
     self.assertEqual(prime, False)

  @weight(1)
  @number("4.6")
  def test_6(self):
        """is_prime_skip_impossible_factors: 1"""
        prime = is_prime_skip_impossible_factors(1)
        self.assertEqual(prime, False)

  @weight(1)
  @number("4.7")
  def test_7(self):
        """is_prime_skip_impossible_factors: All primes less than 100"""
        actualPrimes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        testPrimes=[]
        for n in range(1, 101):
            if is_prime_skip_impossible_factors(n):
                testPrimes.append(n)
        self.assertEqual(testPrimes, actualPrimes)

  @weight(1)
  @number("4.8")
  def test_8(self):
        """is_prime_skip_impossible_factors: Negative Number"""
        prime = is_prime_skip_impossible_factors(-35)
        self.assertEqual(prime, False)