import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

from dinner import invite_to_dinner_optimized

from dinner_solution import invite_to_dinner_optimized_solution, invite_to_dinner_with_ties

class TestDinnerOptimized(unittest.TestCase):
    @weight(1)
    @number("4.1")
    def test_1(self):
        """Invite to Dinner Optimized- friends2"""
        friends={
           'Alice':['Bob'],
           'Bob':['Alice', 'Eve'],
           'Eve':['Bob']
        }
        actual = invite_to_dinner_optimized(friends)
        expected = invite_to_dinner_optimized_solution(friends)
        self.assertEqual(sorted(actual), sorted(expected))

    @weight(1)
    @number("4.2")
    def test_2(self):
        """Invite to Dinner Optimized- friends"""
        friends={
            'Alice':['Bob'],
            'Bob':['Alice', 'Eve'],
            'Cleo':[],
            'Don':[],
            'Eve':['Bob']
        }
        actual = invite_to_dinner_optimized(friends)
        expected = invite_to_dinner_optimized_solution(friends)
        self.assertEqual(sorted(actual), sorted(expected))

    @weight(1)
    @number("4.3")
    def test_3(self):
        """Invite to Dinner Optimized- friends3"""
        friends = {
        'Asa':[], 
        'Bear':['Cate'],
        'Cate':['Bear', 'Dave'],
        'Dave':['Cate','Eve'], 
        'Eve':['Dave'], 
        'Finn':['Ginny', 'Ivan'], 
        'Ginny':['Finn', 'Haruki'], 
        'Haruki':['Ginny'], 
        'Ivan':['Finn']
        }
        actual = invite_to_dinner_optimized(friends)
        expected_possibilities = invite_to_dinner_with_ties(friends)
        self.assertIn(sorted(actual), expected_possibilities)

    @weight(1)
    @number("4.4")
    def test_4(self):
        """Invite to Dinner Optimized- No friends"""
        friends={}
        actual = invite_to_dinner_optimized(friends)
        expected = invite_to_dinner_optimized_solution(friends)
        self.assertEqual(sorted(actual), sorted(expected))

    @weight(1)
    @number("4.5")
    def test_5(self):
        """Invite to Dinner Optimized- No dislikes"""
        friends={
            'Asa':[], 
            'Bear':[],
            'Cate':[],
            'Dave':[], 
            'Eve':[], 
            'Finn':[], 
            'Ginny':[], 
            'Haruki':[], 
            'Ivan':[]
        }
        actual = invite_to_dinner_optimized(friends)
        expected = invite_to_dinner_optimized_solution(friends)
        self.assertEqual(sorted(actual), sorted(expected))

    @weight(1)
    @number("4.6")
    def test_6(self):
        """Invite to Dinner Optimized- One friend disliked by all"""
        friends={
            'Asa':['Haruki'], 
            'Bear':['Haruki'],
            'Cate':['Haruki'],
            'Dave':['Haruki'], 
            'Eve':['Haruki'], 
            'Finn':['Haruki'], 
            'Ginny':['Haruki'], 
            'Haruki':['Ivan', 'Ginny', 'Finn', 'Eve', 'Dave', 'Cate', 'Bear', 'Asa'], 
            'Ivan':['Haruki']
        }
        actual = invite_to_dinner_optimized(friends)
        expected = invite_to_dinner_optimized_solution(friends)
        self.assertEqual(sorted(actual), sorted(expected))

    @weight(1)
    @number("4.7")
    def test_7(self):
        """Invite to Dinner Optimized- Multiple best solutions"""
        friends={
            'Alice':['Bob'],
            'Bob':['Alice'],
            'Cleo':[],
        }
        actual = invite_to_dinner_optimized(friends)
        expected_possibilities = invite_to_dinner_with_ties(friends)
        self.assertIn(sorted(actual), expected_possibilities)