import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

from dinner import find_dislikes

class TestFindDislikes(unittest.TestCase):
    @weight(1)
    @number("1.1")
    def test_1(self):
        """Find Invites- friends2"""
        friends={
           'Alice':['Bob'],
           'Bob':['Alice', 'Eve'],
           'Eve':['Bob']
        }
        actual = find_dislikes(friends)
        expected = {('Alice','Bob'),('Bob','Eve')}
        self.assertEqual(actual, expected)

    @weight(1)
    @number("1.2")
    def test_2(self):
        """Find Invites- friends"""
        friends={
            'Alice':['Bob'],
            'Bob':['Alice', 'Eve'],
            'Cleo':[],
            'Don':[],
            'Eve':['Bob']
        }
        actual = find_dislikes(friends)
        expected = {('Alice','Bob'),('Bob','Eve')}
        self.assertEqual(actual, expected)

    @weight(1)
    @number("1.3")
    def test_3(self):
        """Find Invites- friends_3"""
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
        actual = find_dislikes(friends)
        expected = {('Bear', 'Cate'), ('Cate', 'Dave'), ('Finn', 'Ginny'), ('Ginny', 'Haruki'), ('Finn', 'Haruki'), ('Dave', 'Eve'), ('Finn', 'Ivan')}
        self.assertEqual(actual, expected)

    @weight(1)
    @number("1.4")
    def test_4(self):
        """Find Invites- No friends"""
        friends={}
        actual = find_dislikes(friends)
        expected = set()
        self.assertEqual(actual, expected)

    @weight(1)
    @number("1.5")
    def test_5(self):
        """Find Invites- No dislikes"""
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
        actual = find_dislikes(friends)
        expected = set()
        self.assertEqual(actual, expected)

    @weight(1)
    @number("1.6")
    def test_6(self):
        """Find Invites- One friend disliked by all"""
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
        actual = find_dislikes(friends)
        expected = {('Cate', 'Haruki'), ('Eve', 'Haruki'), ('Haruki', 'Ivan'), ('Bear', 'Haruki'), ('Dave', 'Haruki'), ('Asa', 'Haruki'), ('Ginny', 'Haruki'), ('Finn', 'Haruki')}
        self.assertEqual(actual, expected)

    @weight(1)
    @number("1.7")
    def test_7(self):
        """Find Invites- One-directional connections"""
        friends={
            'Alice':[],
            'Bob':['Alice', 'Eve'],
            'Cleo':[],
            'Don':[],
            'Eve':[]
        }
        actual = find_dislikes(friends)
        expected = {('Alice','Bob'),('Bob','Eve')}
        self.assertEqual(actual, expected)