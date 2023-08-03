import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

from dinner import filter_no_dislikes

class TestFilterNoDislikes(unittest.TestCase):
    @weight(1)
    @number("2.1")
    def test_1(self):
        """filter_no_dislikes- friends2"""
        friends={
           'Alice':['Bob'],
           'Bob':['Alice', 'Eve'],
           'Eve':['Bob']
        }
        actual_no_dislikes, actual_new_friends = filter_no_dislikes(friends)
        expected_no_dislikes = []
        expected_new_friends = friends
        self.assertEqual(sorted(actual_no_dislikes), sorted(expected_no_dislikes))
        self.assertEqual(actual_new_friends, expected_new_friends)


    @weight(1)
    @number("2.2")
    def test_2(self):
        """filter_no_dislikes- friends"""
        friends={
            'Alice':['Bob'],
            'Bob':['Alice', 'Eve'],
            'Cleo':[],
            'Don':[],
            'Eve':['Bob']
        }
        actual_no_dislikes, actual_new_friends = filter_no_dislikes(friends)
        expected_no_dislikes = ['Cleo', 'Don']
        expected_new_friends = {
            'Alice':['Bob'],
            'Bob':['Alice', 'Eve'],
            'Eve':['Bob']
        }
        self.assertEqual(sorted(actual_no_dislikes), sorted(expected_no_dislikes))
        self.assertEqual(actual_new_friends, expected_new_friends)

    @weight(1)
    @number("2.3")
    def test_3(self):
        """filter_no_dislikes- friends_3"""
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
        actual_no_dislikes, actual_new_friends = filter_no_dislikes(friends)
        expected_no_dislikes = ['Asa']
        expected_new_friends = { 
            'Bear':['Cate'],
            'Cate':['Bear', 'Dave'],
            'Dave':['Cate','Eve'], 
            'Eve':['Dave'], 
            'Finn':['Ginny', 'Haruki', 'Ivan'], 
            'Ginny':['Finn','Haruki'], 
            'Haruki':['Ginny'], 
            'Ivan':['Finn']
        }
        self.assertEqual(sorted(actual_no_dislikes), sorted(expected_no_dislikes))
        self.assertEqual(actual_new_friends, expected_new_friends)

    @weight(1)
    @number("2.4")
    def test_4(self):
        """filter_no_dislikes- No friends"""
        friends={}
        actual_no_dislikes, actual_new_friends = filter_no_dislikes(friends)
        expected_no_dislikes = []
        expected_new_friends = friends
        self.assertEqual(sorted(actual_no_dislikes), sorted(expected_no_dislikes))
        self.assertEqual(actual_new_friends, expected_new_friends)

    @weight(1)
    @number("2.5")
    def test_5(self):
        """filter_no_dislikes- No dislikes"""
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
        actual_no_dislikes, actual_new_friends = filter_no_dislikes(friends)
        expected_no_dislikes = ['Asa','Bear','Cate','Dave','Eve','Finn','Ginny','Haruki','Ivan']
        expected_new_friends = {}
        self.assertEqual(sorted(actual_no_dislikes), sorted(expected_no_dislikes))
        self.assertEqual(actual_new_friends, expected_new_friends)

    @weight(1)
    @number("2.6")
    def test_6(self):
        """filter_no_dislikes- One friend disliked by all"""
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
        actual_no_dislikes, actual_new_friends = filter_no_dislikes(friends)
        expected_no_dislikes = []
        expected_new_friends = friends
        self.assertEqual(sorted(actual_no_dislikes), sorted(expected_no_dislikes))
        self.assertEqual(actual_new_friends, expected_new_friends)

    @weight(1)
    @number("2.7")
    def test_7(self):
        """filter_no_dislikes- One-directional connections"""
        friends={
            'Alice':[],
            'Bob':['Alice', 'Eve'],
            'Cleo':[],
            'Don':[],
            'Eve':[]
        }
        actual_no_dislikes, actual_new_friends = filter_no_dislikes(friends)
        expected_no_dislikes = ['Cleo', 'Don']
        expected_new_friends = {
            'Alice':[],
            'Bob':['Alice', 'Eve'],
            'Eve':[]
        }
        self.assertEqual(sorted(actual_no_dislikes), sorted(expected_no_dislikes))
        self.assertEqual(actual_new_friends, expected_new_friends)