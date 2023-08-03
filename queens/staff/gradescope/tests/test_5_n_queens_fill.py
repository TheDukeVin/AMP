import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from queens import n_queens_fill


def noConflicts(board, current):
    for i in range(current):
        if board[i] == board[current]:
            return False
        if current - i == abs(board[current] - board[i]):
            return False
    return True

def testValid(board, inp):
    if board == None:
        return False
    if len(board) != len(inp):
        return False
    for i in range(len(board)):
        if inp[i] >= 0 and board[i] != inp[i] or 0 > board[i] or len(board) <= board[i]:
            return False
    for i in range(len(board)):
        if not noConflicts(board, i):
            return False
    return True


class TestEx1(unittest.TestCase):
    @weight(1)
    @number("5.0")
    def test_01(self):
        """n_queens_fill: Sample: 10x10"""
        N = 10
        inp = [-1, -1, 4, -1, -1, -1, -1, 0, -1, 5]
        board = inp[:]
        toChange = [-1] * N
        v = n_queens_fill(toChange, board, 0)
        if isinstance(v, list):
            val = testValid(v, inp)
            self.assertEqual(val, True)
        else:
            val = testValid(toChange, inp)
            self.assertEqual(val and v, True)



    # @weight(1)
    # @number("5.02")
    # def test_02(self):
    #   """Sample 2: 10x10"""
    #   N=10
    #   inp = [-1, -1, 4, -1, -1, 2]
    #   board = inp[:]
    #   toChange = [-1]*N
    #   n_queens_fill(toChange, board, 0, N)
    #   val = testValid(toChange, inp)
    #   self.assertEqual(val, True)

    @weight(1)
    @number("5.1")
    def test_1(self):
        """n_queens_fill: 3x3 board"""
        N = 3
        inp = [-1, -1, -1]
        board = inp[:]
        toChange = [-1] * N
        v = n_queens_fill(toChange, board)
        self.assertEqual(v, None) # TODO i don't understand this

    @weight(1)
    @number("5.2")
    def test_2(self):
        """n_queens_fill: 4x4 invalid board - no solution"""
        N = 4
        inp = [-1, -1, 2, -1]
        board = inp[:]
        toChange = [-1] * N
        v = n_queens_fill(toChange, board)
        self.assertEqual(v, None)

    @weight(1)
    @number("5.3")
    def test_3(self):
        """n_queens_fill: 4x4 invalid board - input conflicting"""
        N = 4
        inp = [0, 0, -1, -1]
        board = inp[:]
        toChange = [-1] * N
        v = n_queens_fill(toChange, board)
        self.assertEqual(v, None)

    @weight(1)
    @number("5.4")
    def test_4(self):
        """n_queens_fill: 4x4 invalid board - input out of bounds"""
        N = 4
        inp = [0, 4, -1, -1]
        board = inp[:]
        toChange = [-1] * N
        v = n_queens_fill(toChange, board)
        self.assertEqual(v, None)

    @weight(1)
    @number("5.5")
    def test_5(self):
        """n_queens_fill: 6x6 invalid board - no solution"""
        N = 6
        inp = [-1, -1, 2, -1, -1, 1]
        board = inp[:]
        toChange = [-1] * N
        v = n_queens_fill(toChange, board)
        self.assertEqual(v, None)

    @weight(1)
    @number("5.6")
    def test_6(self):
        """n_queens_fill: 12x12 invalid board - no solution"""
        N = 12
        inp = [7, -1, -1, 1, -1, 6, 2, -1, 8, 11, -1, 3]
        board = inp[:]
        toChange = [-1] * N
        v = n_queens_fill(toChange, board)
        self.assertEqual(v, None)

    @weight(1)
    @number("5.7")
    def test_7(self):
        """n_queens_fill: 4x4 valid board"""
        N = 4
        inp = [2, -1, -1, -1]
        board = inp[:]
        toChange = [-1] * N
        v = n_queens_fill(toChange, board)
        if isinstance(v, list):
            val = testValid(v, inp)
            self.assertEqual(val, True)
        else:
            val = testValid(toChange, inp)
            self.assertEqual(val and v, True)

    @weight(1)
    @number("5.8")
    def test_8(self):
        """n_queens_fill: 6x6 valid board"""
        N = 6
        inp = [-1, -1, 4, -1, -1, 2]
        board = inp[:]
        toChange = [-1] * N
        v = n_queens_fill(toChange, board)
        if isinstance(v, list):
            val = testValid(v, inp)
            self.assertEqual(val, True)
        else:
            val = testValid(toChange, inp)
            self.assertEqual(val and v, True)

    @weight(1)
    @number("5.9")
    def test_9(self):
        """n_queens_fill: 12x12 valid board"""
        N = 12
        inp = [-1, 9, 6, 1, 7, 2, 0, 8, 4, -1, 3, 10]
        board = inp[:]
        toChange = [-1] * N
        v = n_queens_fill(toChange, board)
        if isinstance(v, list):
            val = testValid(v, inp)
            self.assertEqual(val, True)
        else:
            val = testValid(toChange, inp)
            self.assertEqual(val and v, True)

    @weight(1)
    @number("5.10")
    def test_10(self):
        """n_queens_fill: 12x12 valid board"""
        N = 12
        inp = [-1, 9, -1, -1, 3, 8, -1, 2, 4, -1, -1, -1]
        board = inp[:]
        toChange = [-1] * N
        v = n_queens_fill(toChange, board)
        if isinstance(v, list):
            val = testValid(v, inp)
            self.assertEqual(val, True)
        else:
            val = testValid(toChange, inp)
            self.assertEqual(val and v, True)

    @weight(1)
    @number("5.11")
    def test_11(self):
        """n_queens_fill: 20x20 valid board"""
        N = 20
        inp = [5,-1,-1,-1,6,8,-1,-1,17,-1,14,-1,-1,-1,7,-1,11,9,-1,13]
        board = inp[:]
        toChange = [-1] * N
        v = n_queens_fill(toChange, board)
        if isinstance(v, list):
            val = testValid(v, inp)
            self.assertEqual(val, True)
        else:
            val = testValid(toChange, inp)
            self.assertEqual(val and v, True)
