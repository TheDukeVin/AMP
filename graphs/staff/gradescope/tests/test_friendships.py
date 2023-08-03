import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

from friendships import no_imaginary, friends, self_love, count_friends, antisocial_social_club

b = "Bill"
t = "Ted"
a = "Ana"
f = "Freddie"
g = "Greta"
real_people = [b, t, a, f]

class TestArithmeticSequence(unittest.TestCase):
    @weight(1)
    @number("1")
    def test_imaginary(self):
        """Imaginary - Noone likes anyone imaginary"""
        good_examples = [
            (real_people, []),
            (real_people, [(b,t), (t,b)]),
            (real_people, [(b,t), (t,b), (a,f), (f,a)]),         
            (real_people, [(b,t), (t,a), (a,f)])
        ]
        bad_examples = [
            (real_people, [(g, a)]),
            (real_people, [(a, g)]),
            (real_people, [(b,t), (t,b), (a,f), (g,a)]),
            (real_people, [(b,t), (t,b), (a, g), (a,f), (f,a)])
        ]
        for (p, l) in good_examples:
            self.assertEqual(True, no_imaginary(p,l))

        for (p, l) in bad_examples:
            self.assertEqual(False, no_imaginary(p,l))
        
        
        self.assertEqual(True, no_imaginary(["Ted", "Bill"], [("Ted", "Bill"), ("Bill", "Bill")]))
        self.assertEqual(True, no_imaginary(["John", "Joe", "Larry", "Bob"], [("John", "Joe")]))
        self.assertEqual(False, no_imaginary(["Ted"], [("Ted","Acathla the Friendly Demon")]))
        self.assertEqual(False, no_imaginary(["John", "Joe"], [("John", "Jack")])) 
        self.assertEqual(True, no_imaginary(["Sarah", "Sally"], [("Sarah", "Sally"), ("Sally", "Sarah")]))

    @weight(1)
    @number("2")
    def test_friends(self):
        """Friends - All "liking" is mutual"""
        good_examples = [
            [],
            [(b,t), (t,b)],
            [(b,t), (t,b), (a,f), (f, a)],           
            [(b,t), (t,b), (a,f), (f, a), (g, t), (t, g)]
        ]
        bad_examples = [
            [(g, a)],
            [(a, g)],
            [(g, a), (b, t), (t, b)],
            [(b, t), (t, b), (a, f), (f,a), (g, t)]
        ]
        for l in good_examples:
            self.assertEqual(True, friends(l))

        for l in bad_examples:
            self.assertEqual(False, friends(l))
        
        self.assertEqual(True, friends([("Bill","Ted"),("Ted","Bill")]))
        self.assertEqual(False, friends([("Bill","Ted")]))
        self.assertEqual(False, friends([("Amy","Anna"),("Anna","Amy"),("Amy","Sally")]))
        self.assertEqual(True, friends([("Sue","Bob"),("Bob","Sue"),("Tim","Tina"),("Tina","Tim")]))
        self.assertEqual(False, friends([("Sue","Bob"),("Bob","Sue"),("Tim","Tina"),("Tina","Tim"), ("Tim", "George"), ("George", "Tim"), ("Tim", "Timothy")]))
        self.assertEqual(True, friends([("Sue","Bob"),("Bob","Sue"),("Tim","Tina"),("Tina","Tim"), ("Tim", "George"), ("George", "Tim"), ("Tim", "Tim")]))

    @weight(1)
    @number("3")
    def test_self_love(self):
        """Self_love - dont like your own posts"""
        examples = [
            ([],[]),
            ([(g,g)], []),
            ([(g,g), (a,a)], []),
            ([(a,g),(g,a), (a,f)], [(a,g), (g,a), (a,f)]),
            ([(a,g), (g,a), (a,f), (g,g), (a,a), (f,f)], [(a,g), (g,a), (a,f)])
        ]
        for ins,outs in examples:
            self.assertEqual(sorted(outs), sorted(self_love(ins)))

        self.assertEqual(self_love([("me","me")]), [])
        self.assertEqual(self_love([("you", "me"), ("me","you"), ("you", "you")]), [("you", "me"), ("me", "you")])
        self.assertEqual(self_love([("John", "John"),("John", "John"), ("George", "John")]), [("George", "John")])
        self.assertEqual(self_love([("Sarah", "Sarah"), ("Sarah", "John"), ("John", "Sarah")]), [("Sarah", "John"), ("John", "Sarah")])

    @weight(1)
    @number("4")
    def test_antisocial_social_club(self):
        """Antisocial Social Club -- make the misanthropes hang out together"""
        examples = [
            {"people": real_people,
             "likes": [],
             "misanthropes": real_people
            },
            {"people": real_people,
             "likes": [(b,t),(t,b)],
             "misanthropes": [a,f]
            },           
            {"people": real_people,
             "likes": [(b,t),(f,a)],
             "misanthropes": [t,a]
            }
        ]
        for ex in examples:
            self.assertEqual(sorted(ex["misanthropes"]),
                             sorted(antisocial_social_club(ex["people"], ex["likes"])))

        self.assertEqual(antisocial_social_club(["Jen", "Amy", "Ms. Anthrope", "Isa Lated"], [("Jen","Amy"), ("Amy", "Jen")]), ["Ms. Anthrope", "Isa Lated"])
        self.assertEqual(antisocial_social_club(["Jen", "Amy", "Ms. Anthrope"], [("Jen","Ms. Anthrope"), ("Amy", "Ms. Anthrope")]), ["Ms. Anthrope"])
        self.assertEqual(antisocial_social_club(["John", "Jack", "Joe"], []), ["John", "Jack", "Joe"])
        self.assertEqual(antisocial_social_club(["Sally", "Sarah", "Sue"], [("Sally", "Sarah")]), ["Sarah", "Sue"])
    
    @weight(1)
    @number("5")
    def test_count_friends(self):
        """Do it for the clout -- how many friends does everyone have?"""
        examples = [
            {"people": [b,a,t,f],
             "likes": [],
             "counts": [0,0,0,0]
            },
            {"people": [b,a,t,f],
             "likes": [(b, a), (a, b)],
             "counts": [1,1,0,0]
            },           
            {"people": [b,a,t,f],
             "likes": [(b,t),(f,a)],
             "counts": [0,0,0,0]
            },
            {"people": [b,a,t,f],
             "likes": [(b,t),(t,b), (a, t), (t,a), (f, b)],
             "counts": [1,1,2,0]
            },
        ]
        for ex in examples:
            self.assertEqual(ex["counts"], count_friends(ex["people"], ex["likes"]))
        
        self.assertEqual(count_friends(["Bill","Ted","Ana"], [("Bill","Ted"), ("Ted", "Bill"), ("Ana", "Ted"), ("Ted", "Ana")]), [1, 2, 1])
        self.assertEqual(count_friends(["Bill", "Ted", "Ana"], []), [0, 0, 0])
        self.assertEqual(count_friends(["John", "Jack", "Joe"], [("John", "Jack"), ("Jack", "John"), ("Joe", "John"), ("John", "Joe")]), [2, 1, 1])
        self.assertEqual(count_friends(["Sarah", "Sally", "Sue", "Sandra"], [("Sarah", "Sally"), ("Sally", "Sue"), ("Sue", "Sandra"), ("Sandra", "Sarah")]), [0, 0, 0, 0])

if __name__ == "__main__":
    unittest.main()
                             