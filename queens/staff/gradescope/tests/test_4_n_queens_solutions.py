import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from queens import n_queens_solutions

solutions_3=[]
solutions_4=[[1, 3, 0, 2], [2, 0, 3, 1]]
solutions_5=[[0, 2, 4, 1, 3], [0, 3, 1, 4, 2], [1, 3, 0, 2, 4], [1, 4, 2, 0, 3], [2, 0, 3, 1, 4], [2, 4, 1, 3, 0], [3, 0, 2, 4, 1], [3, 1, 4, 2, 0], [4, 1, 3, 0, 2], [4, 2, 0, 3, 1]]
solutions_6=[[1, 3, 5, 0, 2, 4], [2, 5, 1, 4, 0, 3], [3, 0, 4, 1, 5, 2], [4, 2, 0, 5, 3, 1]]
solutions_8=[[0, 4, 7, 5, 2, 6, 1, 3], [0, 5, 7, 2, 6, 3, 1, 4], [0, 6, 3, 5, 7, 1, 4, 2], [0, 6, 4, 7, 1, 3, 5, 2], [1, 3, 5, 7, 2, 0, 6, 4], [1, 4, 6, 0, 2, 7, 5, 3], [1, 4, 6, 3, 0, 7, 5, 2], 
             [1, 5, 0, 6, 3, 7, 2, 4], [1, 5, 7, 2, 0, 3, 6, 4], [1, 6, 2, 5, 7, 4, 0, 3], [1, 6, 4, 7, 0, 3, 5, 2], [1, 7, 5, 0, 2, 4, 6, 3], [2, 0, 6, 4, 7, 1, 3, 5], [2, 4, 1, 7, 0, 6, 3, 5], 
             [2, 4, 1, 7, 5, 3, 6, 0], [2, 4, 6, 0, 3, 1, 7, 5], [2, 4, 7, 3, 0, 6, 1, 5], [2, 5, 1, 4, 7, 0, 6, 3], [2, 5, 1, 6, 0, 3, 7, 4], [2, 5, 1, 6, 4, 0, 7, 3], [2, 5, 3, 0, 7, 4, 6, 1], 
             [2, 5, 3, 1, 7, 4, 6, 0], [2, 5, 7, 0, 3, 6, 4, 1], [2, 5, 7, 0, 4, 6, 1, 3], [2, 5, 7, 1, 3, 0, 6, 4], [2, 6, 1, 7, 4, 0, 3, 5], [2, 6, 1, 7, 5, 3, 0, 4], [2, 7, 3, 6, 0, 5, 1, 4],
             [3, 0, 4, 7, 1, 6, 2, 5], [3, 0, 4, 7, 5, 2, 6, 1], [3, 1, 4, 7, 5, 0, 2, 6], [3, 1, 6, 2, 5, 7, 0, 4], [3, 1, 6, 2, 5, 7, 4, 0], [3, 1, 6, 4, 0, 7, 5, 2], [3, 1, 7, 4, 6, 0, 2, 5], 
             [3, 1, 7, 5, 0, 2, 4, 6], [3, 5, 0, 4, 1, 7, 2, 6], [3, 5, 7, 1, 6, 0, 2, 4], [3, 5, 7, 2, 0, 6, 4, 1], [3, 6, 0, 7, 4, 1, 5, 2], [3, 6, 2, 7, 1, 4, 0, 5], [3, 6, 4, 1, 5, 0, 2, 7], 
             [3, 6, 4, 2, 0, 5, 7, 1], [3, 7, 0, 2, 5, 1, 6, 4], [3, 7, 0, 4, 6, 1, 5, 2], [3, 7, 4, 2, 0, 6, 1, 5], [4, 0, 3, 5, 7, 1, 6, 2], [4, 0, 7, 3, 1, 6, 2, 5], [4, 0, 7, 5, 2, 6, 1, 3], 
             [4, 1, 3, 5, 7, 2, 0, 6], [4, 1, 3, 6, 2, 7, 5, 0], [4, 1, 5, 0, 6, 3, 7, 2], [4, 1, 7, 0, 3, 6, 2, 5], [4, 2, 0, 5, 7, 1, 3, 6], [4, 2, 0, 6, 1, 7, 5, 3], [4, 2, 7, 3, 6, 0, 5, 1],
             [4, 6, 0, 2, 7, 5, 3, 1], [4, 6, 0, 3, 1, 7, 5, 2], [4, 6, 1, 3, 7, 0, 2, 5], [4, 6, 1, 5, 2, 0, 3, 7], [4, 6, 1, 5, 2, 0, 7, 3], [4, 6, 3, 0, 2, 7, 5, 1], [4, 7, 3, 0, 2, 5, 1, 6], 
             [4, 7, 3, 0, 6, 1, 5, 2], [5, 0, 4, 1, 7, 2, 6, 3], [5, 1, 6, 0, 2, 4, 7, 3], [5, 1, 6, 0, 3, 7, 4, 2], [5, 2, 0, 6, 4, 7, 1, 3], [5, 2, 0, 7, 3, 1, 6, 4], [5, 2, 0, 7, 4, 1, 3, 6], 
             [5, 2, 4, 6, 0, 3, 1, 7], [5, 2, 4, 7, 0, 3, 1, 6], [5, 2, 6, 1, 3, 7, 0, 4], [5, 2, 6, 1, 7, 4, 0, 3], [5, 2, 6, 3, 0, 7, 1, 4], [5, 3, 0, 4, 7, 1, 6, 2], [5, 3, 1, 7, 4, 6, 0, 2], 
             [5, 3, 6, 0, 2, 4, 1, 7], [5, 3, 6, 0, 7, 1, 4, 2], [5, 7, 1, 3, 0, 6, 4, 2], [6, 0, 2, 7, 5, 3, 1, 4], [6, 1, 3, 0, 7, 4, 2, 5], [6, 1, 5, 2, 0, 3, 7, 4], [6, 2, 0, 5, 7, 4, 1, 3], 
             [6, 2, 7, 1, 4, 0, 5, 3], [6, 3, 1, 4, 7, 0, 2, 5], [6, 3, 1, 7, 5, 0, 2, 4], [6, 4, 2, 0, 5, 7, 1, 3], [7, 1, 3, 0, 6, 4, 2, 5], [7, 1, 4, 2, 0, 6, 3, 5], [7, 2, 0, 5, 1, 4, 6, 3], [7, 3, 0, 2, 5, 1, 6, 4]]

class TestEx1(unittest.TestCase):
  @weight(1)
  @number("4.1")
  def test_1(self):
    """4 queens, num_sol=2"""
    board_size = 4
    num_sol = 2
    actual_sols=[]
    n_queens_solutions(board_size, num_sol, actual_sols)
    expected_sols = solutions_4
    print(f"Length of solutions list should be {min(num_sol, len(expected_sols))}", end=" ")
    self.assertEqual(len(actual_sols), min(num_sol, len(expected_sols)))
    print("OK")
    print(f"Checking for unique solutions...")
    for solution in expected_sols:
      print(f"{solution}", end=" ")
      self.assertIn(solution, actual_sols)
      print("OK")

  @weight(1)
  @number("4.2")
  def test_2(self):
    """4 queens, num_sol=1"""
    board_size = 4
    num_sol = 1
    actual_sols=[]
    n_queens_solutions(board_size, num_sol, actual_sols)
    expected_sols = solutions_4
    print(f"Length of solutions list should be {min(num_sol, len(expected_sols))}", end=" ")
    self.assertEqual(len(actual_sols), min(num_sol, len(expected_sols)))
    print("OK")
    print(f"Checking for unique solutions...")
    for solution in actual_sols: #every actual solution should be in expected solution
      print(f"{solution}", end=" ")
      self.assertIn(solution, expected_sols)
      print("OK")

  @weight(1)
  @number("4.3")
  def test_3(self):
    """4 queens, num_sol=29"""
    board_size = 4
    num_sol = 29
    actual_sols=[]
    n_queens_solutions(board_size, num_sol, actual_sols)
    expected_sols = solutions_4
    print(f"Length of solutions list should be {min(num_sol, len(expected_sols))}", end=" ")
    self.assertEqual(len(actual_sols), min(num_sol, len(expected_sols)))
    print("OK")
    print(f"Checking for unique solutions...")
    for solution in expected_sols:
      print(f"{solution}", end=" ")
      self.assertIn(solution, actual_sols)
      print("OK")
  
  @weight(1)
  @number("4.4")
  def test_4(self):
    """8 queens, num_sol=50"""
    board_size = 8
    num_sol = 50
    actual_sols=[]
    n_queens_solutions(board_size, num_sol, actual_sols)
    expected_sols = solutions_8
    print(f"Length of solutions list should be {min(num_sol, len(expected_sols))}", end=" ")
    self.assertEqual(len(actual_sols), min(num_sol, len(expected_sols)))
    print("OK")
    print(f"Checking for unique solutions...")
    for solution in actual_sols: #every actual solution should be in expected solution
      print(f"{solution}", end=" ")
      self.assertIn(solution, expected_sols)
      print("OK")

  @weight(1)
  @number("4.5")
  def test_5(self):
    """8 queens, num_sol=1000"""
    board_size = 8
    num_sol = 1000
    actual_sols=[]
    n_queens_solutions(board_size, num_sol, actual_sols)
    expected_sols = solutions_8
    print(f"Length of solutions list should be {min(num_sol, len(expected_sols))}", end=" ")
    self.assertEqual(len(actual_sols), min(num_sol, len(expected_sols)))
    print("OK")
    print(f"Checking for unique solutions...")
    for solution in expected_sols: #every expected solution should be in actual solution
      print(f"{solution}", end=" ")
      self.assertIn(solution, actual_sols)
      print("OK")

  @weight(1)
  @number("4.6")
  def test_6(self):
    """8 queens, num_sol=1"""
    board_size = 8
    num_sol = 1
    actual_sols=[]
    n_queens_solutions(board_size, num_sol, actual_sols)
    expected_sols = solutions_8
    print(f"Length of solutions list should be {min(num_sol, len(expected_sols))}", end=" ")
    self.assertEqual(len(actual_sols), min(num_sol, len(expected_sols)))
    print("OK")
    print(f"Checking for unique solutions...")
    for solution in actual_sols:
      print(f"{solution}", end=" ")
      self.assertIn(solution, expected_sols)
      print("OK")

  @weight(1)
  @number("4.7")
  def test_7(self):
    """6 queens, num_sol=1"""
    board_size = 6
    num_sol = 1
    actual_sols=[]
    n_queens_solutions(board_size, num_sol, actual_sols)
    expected_sols = solutions_6
    print(f"Length of solutions list should be {min(num_sol, len(expected_sols))}", end=" ")
    self.assertEqual(len(actual_sols), min(num_sol, len(expected_sols)))
    print("OK")
    print(f"Checking for unique solutions...")
    for solution in actual_sols:
      print(f"{solution}", end=" ")
      self.assertIn(solution, expected_sols)
      print("OK")

  @weight(1)
  @number("4.8")
  def test_8(self):
    """6 queens, num_sol=500"""
    board_size = 6
    num_sol = 500
    actual_sols=[]
    n_queens_solutions(board_size, num_sol, actual_sols)
    expected_sols = solutions_6
    print(f"Length of solutions list should be {min(num_sol, len(expected_sols))}", end=" ")
    self.assertEqual(len(actual_sols), min(num_sol, len(expected_sols)))
    print("OK")
    print(f"Checking for unique solutions...")
    for solution in expected_sols: #every expected solution should be in actual solution
      print(f"{solution}", end=" ")
      self.assertIn(solution, actual_sols)
      print("OK")

  @weight(1)
  @number("4.9")
  def test_9(self):
    """5 queens, num_sol=5"""
    board_size = 5
    num_sol = 5
    actual_sols=[]
    n_queens_solutions(board_size, num_sol, actual_sols)
    expected_sols = solutions_5
    print(f"Length of solutions list should be {min(num_sol, len(expected_sols))}", end=" ")
    self.assertEqual(len(actual_sols), min(num_sol, len(expected_sols)))
    print("OK")
    print(f"Checking for unique solutions...")
    for solution in actual_sols: #every actual solution should be in expected solution
      print(f"{solution}", end=" ")
      self.assertIn(solution, expected_sols)
      print("OK")

  @weight(1)
  @number("4.10")
  def test_10(self):
    """5 queens, num_sol=555"""
    board_size = 5
    num_sol = 555
    actual_sols=[]
    n_queens_solutions(board_size, num_sol, actual_sols)
    expected_sols = solutions_5
    self.assertEqual(len(actual_sols), min(num_sol, len(expected_sols)))
    for solution in expected_sols: #every expected solution should be in actual solution
      self.assertIn(solution, actual_sols)

  @weight(1)
  @number("4.11")
  def test_11(self):
    """3 queens, num_sol=10"""
    board_size = 3
    num_sol = 10
    actual_sols=[]
    n_queens_solutions(board_size, num_sol, actual_sols)
    expected_sols = solutions_3
    self.assertEqual(len(actual_sols), min(num_sol, len(expected_sols)))
    for solution in expected_sols: #every expected solution should be in actual solution
      self.assertIn(solution, actual_sols)


  @weight(1)
  @number("4.12")
  def test_12(self):
    """9, 10, 11, 12, 13 queens"""
    board_sizes = [9, 10, 11, 12, 13]
    num_sols = [352, 724, 2680, 14200, 73712]

    for index, board_size in enumerate(board_sizes):
      actual_sols=[]
      n_queens_solutions(board_size, 100000, actual_sols)
      expected_sol= num_sols[index]
      self.assertEqual(len(actual_sols), expected_sol)