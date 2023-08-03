import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from queens import eight_queens_solutions

def noConflicts(board, current):
  for i in range(current):
    if (board[i] == board[current]):
      return False
    if (current - i == abs(board[current] - board[i])):
      return False
  return True

# Steps:
# Is the number returned correct?
  # There are 92 total for EightQueens
# Do any two returned repeat?
# For each returned:
  # Are the rows in range?
  # Are there conflicts?

class TestEx1(unittest.TestCase):
  @weight(1)
  @number("3.1")
  def test_1(self):
    """eight_queens_solutions: Number returned is correct"""
    N = 29
    val = len(eight_queens_solutions(N))
    self.assertEqual(val, N)

  @weight(1)
  @number("3.2")
  def test_2(self):
    """eight_queens_solutions: No repeated among returned"""
    N = 50
    val = eight_queens_solutions(N)
    val = {tuple(x) for x in val}
    val = len(val)
    self.assertEqual(val, N)

  @weight(1)
  @number("3.3")
  def test_3(self):
    """eight_queens_solutions: All columns in range [0, 8)"""
    N, val = 31, True
    ret = eight_queens_solutions(N)
    for x in ret:
      for y in x:
        if 0 > y or 8 <= y:
          val = False
    self.assertEqual(val, True)

  @weight(1)
  @number("3.4")
  def test_4(self):
    """eight_queens_solutions: No conflicts among returned"""
    N, notConflicting = 31, 0
    ret = eight_queens_solutions(N)
    for x in ret:
      works = True
      for i in range(8):
        if not noConflicts(x, i):
          works = False
      if works:
        notConflicting += 1
    self.assertEqual(notConflicting, 31)

  @weight(1)
  @number("3.5")
  def test_5(self):
    """eight_queens_solutions: More requested than possible"""
    N, notConflicting = 101, 0
    ret = eight_queens_solutions(N)
    for x in ret:
      works = True
      for i in range(8):
        if not noConflicts(x, i):
          works = False
      if works:
        notConflicting += 1
    self.assertEqual(notConflicting, 92)
