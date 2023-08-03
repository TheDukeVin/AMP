import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from queens import no_collisions

def EightQueensIterative(n=8):
    '''
    Starter solution for the 8-Queens puzzle.
    '''
    solutions=[]
    board = [-1] * n
    for i in range(n):
        board[0] = i
        for j in range(n):
            board[1] = j
            if not no_collisions(board, 1):
                continue
            for k in range(n):
                board[2] = k
                if not no_collisions(board, 2):
                    continue
                for l in range(n):
                    board[3] = l
                    if not no_collisions(board, 3):
                        continue
                    for m in range(n):
                        board[4] = m
                        if not no_collisions(board, 4):
                            continue
                        for o in range(n):
                            board[5] = o
                            if not no_collisions(board, 5):
                                continue
                            for p in range(n):
                                board[6] = p
                                if not no_collisions(board, 6):
                                    continue
                                for q in range(n):
                                    board[7] = q
                                    if no_collisions(board, 7):
                                        solutions.append(board[:])
    return solutions

class TestEx1(unittest.TestCase):
  @weight(1)
  @number("2.1")
  def test_1(self):
    """No conflicts - 1x1"""
    board = [0]
    val = no_collisions(board, 0)
    self.assertEqual(val, True)

  @weight(1)
  @number("2.2")
  def test_2(self):
    """No conflicts - 8x8, current = 2"""
    board = [3, 6, 4, -1, -1, -1, -1, -1]
    val = no_collisions(board, 2)
    self.assertEqual(val, True)

  @weight(1)
  @number("2.3")
  def test_3(self):
    """No conflicts - 8x8, current = 7"""
    board = [4, 0, 7, 3, 1, 6, 2, 5]
    val = no_collisions(board, 7)
    self.assertEqual(val, True)

  @weight(1)
  @number("2.4")
  def test_4(self):
    """No conflicts - 15x15, current = 12"""
    board = [8, 0, 2, 4, 6, 10, 12, 14, 1, 5, 13, 9, 7, -1, -1]
    val = no_collisions(board, 12)
    self.assertEqual(val, True)

  @weight(1)
  @number("2.5")
  def test_5(self):
    """Conflicts - value out of bounds"""
    board = [4, 0, 8, -1, -1, -1, -1, -1]
    val = no_collisions(board, 2)
    self.assertEqual(val, False)

  @weight(1)
  @number("2.6")
  def test_6(self):
    """Conflicts - same row"""
    board = [3, 0, 3, -1, -1, -1, -1, -1]
    val = no_collisions(board, 2)
    self.assertEqual(val, False)

  @weight(1)
  @number("2.7")
  def test_7(self):
    """Conflicts - diagonal 1"""
    board = [3, 0, 6, 7, -1, -1, -1, -1]
    val = no_collisions(board, 3)
    self.assertEqual(val, False)

  @weight(1)
  @number("2.8")
  def test_8(self):
    """Conflicts - diagonal 2"""
    board = [3, 0, 6, 4, 2, 7, 5, 1]
    val = no_collisions(board, 7)
    self.assertEqual(val, False)

  @weight(1)
  @number("2.9")
  def test_9(self):
       """Conflicts - diagonal 2"""
       board = [7, 6, 5, 4, 3, 2, 1, 0]
       val = no_collisions(board, 7)
       self.assertEqual(val, False)

  @weight(1)
  @number("2.10")
  def test_10(self):
    """Conflicts - diagonal 2"""
    board = [0,1,2,3,4,5,-1,-1]
    val = no_collisions(board, 5)
    self.assertEqual(val, False)

  @weight(1)
  @number("2.11")
  def test_11(self):
      """Correct number of solutions for 8Queens iterative"""
      solutions = EightQueensIterative()
      val = len(solutions)
      self.assertEqual(val, 92)
