import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

from dinner import filter_bad_invites
from dinner_solution import generate_all_subsets_solution, filter_bad_invites_solution

class TestFilterBadInvites(unittest.TestCase):
    @weight(1)
    @number("3.1")
    def test_1(self):
        """Filter Bad Invites- friends2"""
        friends={
           'Alice':['Bob'],
           'Bob':['Alice', 'Eve'],
           'Eve':['Bob']
        }
        all_subsets = generate_all_subsets_solution(friends)

        actual = filter_bad_invites(all_subsets, friends)
        expected = filter_bad_invites_solution(all_subsets, friends)

        self.assertEqual(sorted(actual), sorted(expected))

    @weight(1)
    @number("3.2")
    def test_2(self):
        """Filter Bad Invites- friends"""
        friends={
            'Alice':['Bob'],
            'Bob':['Alice', 'Eve'],
            'Cleo':[],
            'Don':[],
            'Eve':['Bob']
        }
        all_subsets = generate_all_subsets_solution(friends)

        actual = filter_bad_invites(all_subsets, friends)
        expected = filter_bad_invites_solution(all_subsets, friends)
        
        self.assertEqual(sorted(actual), sorted(expected))

    @weight(1)
    @number("3.3")
    def test_3(self):
        """Filter Bad Invites- friends_3"""
        friends={
        'Asa':[], 
        'Bear':['Cate'],
        'Cate':['Bear', 'Dave'],
        'Dave':['Cate','Eve'], 
        'Eve':['Dave'], 
        'Finn':['Ginny', 'Haruki', 'Ivan'], 
        'Ginny':['Finn','Haruki'], 
        'Haruki':['Ginny'], 
        'Ivan':['Finn']
        }
        all_subsets = generate_all_subsets_solution(friends)

        actual = filter_bad_invites(all_subsets, friends)
        expected = filter_bad_invites_solution(all_subsets, friends)
        
        self.assertEqual(sorted(actual), sorted(expected))

    @weight(1)
    @number("3.4")
    def test_4(self):
        """Filter Bad Invites- No friends"""
        friends={}
        all_subsets = generate_all_subsets_solution(friends)

        actual = filter_bad_invites(all_subsets, friends)
        expected = filter_bad_invites_solution(all_subsets, friends)
        
        self.assertEqual(sorted(actual), sorted(expected))

    @weight(1)
    @number("3.5")
    def test_5(self):
        """Filter Bad Invites- No dislikes"""
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
        all_subsets = generate_all_subsets_solution(friends)

        actual = filter_bad_invites(all_subsets, friends)
        expected = filter_bad_invites_solution(all_subsets, friends)
        
        self.assertEqual(sorted(actual), sorted(expected))

    @weight(1)
    @number("3.6")
    def test_6(self):
        """Filter Bad Invites- One friend disliked by all"""
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
        all_subsets = generate_all_subsets_solution(friends)

        actual = filter_bad_invites(all_subsets, friends)
        expected = filter_bad_invites_solution(all_subsets, friends)
        
        self.assertEqual(sorted(actual), sorted(expected))

    @weight(1)
    @number("3.7")
    def test_7(self):
        """Filter Bad Invites- One-directional connections"""
        friends={
            'Alice':[],
            'Bob':['Alice', 'Eve'],
            'Cleo':[],
            'Don':[],
            'Eve':[]
        }
        all_subsets = generate_all_subsets_solution(friends)

        actual = filter_bad_invites(all_subsets, friends)
        expected = filter_bad_invites_solution(all_subsets, friends)
        
        self.assertEqual(sorted(actual), sorted(expected))