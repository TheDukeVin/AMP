import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from queens import pretty_print

class TestEx1(unittest.TestCase):
  @weight(1)
  @number("1.1")
  def test_1(self):
    """pretty_print: 1x1 board"""
    board = [0]
    desired_val = "\nQ\n"
    val = pretty_print(board)
    self.assertEqual(val, desired_val)

  @weight(1)
  @number("1.2")
  def test_2(self):
    """pretty_print: 4x4 board 1"""
    board = [1, 3, 0, 2]
    desired_val = "\n..Q.\nQ...\n...Q\n.Q..\n"
    val = pretty_print(board)
    self.assertEqual(val, desired_val)

  @weight(1)
  @number("1.3")
  def test_3(self):
    """pretty_print: 4x4 board 2"""
    board = [2, 0, 3, 1]
    desired_val = "\n.Q..\n...Q\nQ...\n..Q.\n"
    val = pretty_print(board)
    self.assertEqual(val, desired_val)

  @weight(1)
  @number("1.3")
  def test_3(self):
    """6x6 board with empty spots at the end"""
    board = [3, 0, 4, 1, -1, -1]
    desired_val = "\n.Q....\n...Q..\n......\nQ.....\n..Q...\n......\n"
    val = pretty_print(board)
    self.assertEqual(val, desired_val)

  @weight(1)
  @number("1.4")
  def test_4(self):
    """8x8 board  with empty spots scattered around the board"""
    board = [-1, 4, -1, 3, 0, -1, 1, 5]
    desired_val = "\n....Q...\n......Q.\n........\n...Q....\n.Q......\n.......Q\n........\n........\n"
    val = pretty_print(board)
    self.assertEqual(val, desired_val)

  @weight(1)
  @number("1.5")
  def test_5(self):
    """pretty_print: 8x8 board with no empty spots"""
    board = [7, 1, 3, 0, 6, 4, 2, 5]
    desired_val = "\n...Q....\n.Q......\n......Q.\n..Q.....\n.....Q..\n.......Q\n....Q...\nQ.......\n"
    
    val = pretty_print(board)
    self.assertEqual(val, desired_val)

  @weight(1)
  @number("1.6")
  def test_6(self):
    """pretty_print: 15x15 board - odd sized, large board"""
    board = [5, 0, 6, 4, 11, 14, 3, 13, 8, 12, 2, 7, 10, 1, 9]
    desired_val = '\n.Q.............\n.............Q.\n..........Q....\n......Q........\n...Q...........\nQ..............\n..Q............\n...........Q...\n........Q......\n..............Q\n............Q..\n....Q..........\n.........Q.....\n.......Q.......\n.....Q.........\n'
    val = pretty_print(board)
    self.assertEqual(val, desired_val)