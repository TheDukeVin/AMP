import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from prime_timing import is_prime_skip_evens

class TestEx1(unittest.TestCase):
  @weight(1)
  @number("3.1")
  def test_1(self):
      """is_prime_skip_evens: Single Even Composite Number"""
      prime = is_prime_skip_evens(12)
      self.assertEqual(prime, False)

  @weight(1)
  @number("3.2")
  def test_2(self):
      """is_prime_skip_evens: Single Odd Prime Number"""
      prime = is_prime_skip_evens(17)
      self.assertEqual(prime, True)

  @weight(1)
  @number("3.3")
  def test_3(self):
      """is_prime_skip_evens: Single Even Prime Number"""
      prime = is_prime_skip_evens(2)
      self.assertEqual(prime, True)

  @weight(1)
  @number("3.4")
  def test_4(self):
      """is_prime_skip_evens: Single Odd Composite Number"""
      prime = is_prime_skip_evens(35)
      self.assertEqual(prime, False)

  @weight(1)
  @number("3.5")
  def test_5(self):
     """is_prime_skip_evens: 0"""
     prime = is_prime_skip_evens(0)
     self.assertEqual(prime, False)

  @weight(1)
  @number("3.6")
  def test_6(self):
        """is_prime_skip_evens: 1"""
        prime = is_prime_skip_evens(1)
        self.assertEqual(prime, False)

  @weight(1)
  @number("3.7")
  def test_7(self):
        """is_prime_skip_evens: All primes less than 100"""
        actualPrimes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        testPrimes=[]
        for n in range(1, 101):
            if is_prime_skip_evens(n):
                testPrimes.append(n)
        prime = is_prime_skip_evens(-17)
        self.assertEqual(testPrimes, actualPrimes)

  @weight(1)
  @number("3.8")
  def test_8(self):
        """is_prime_skip_evens: Negative Number"""
        prime = is_prime_skip_evens(-35)
        self.assertEqual(prime, False)