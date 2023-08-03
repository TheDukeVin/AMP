import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

from random import shuffle
from change import count_change, make_smart_change_best, make_change


class TestChange(unittest.TestCase):

    def cannonicalize(self,change_alternatives):
        """
        cannonicallize a list of change to be order agnostic
        """
        return set(tuple(sorted(list(change))) for change in change_alternatives)

    def assertCannonicallyEqual(self, correct, student):
        """
        testing that two lists of lists are equivalent when cast as sets of sets
        """
        shuffle(student)
        shuffle(correct)
        self.assertEqual(self.cannonicalize(correct), self.cannonicalize(student))

    @weight(1)
    @number("1")
    def test_make_change(self):
        """
        Testing Make Change. The "First set" is the ways of making change, the "Second set" is your solution
        """
        bills = [1, 2, 5]
        self.assertCannonicallyEqual([(1, 1, 1, 1, 1, 1), (1, 1, 1, 1, 2), (1, 1, 2, 2), (1, 5), (2, 2, 2)],
                                      make_change(bills,6))

        bills = [1, 2, 3, 4, 5]
        self.assertCannonicallyEqual([(1, 1, 1, 1, 1, 1), (1, 1, 1, 1, 2), (1, 1, 1, 3), (1, 1, 2, 2), (1, 1, 4), (1, 2, 3), (1,5), (2, 2, 2), (2,4), (3, 3)], 
                                     make_change(bills,6))

        bills = [1, 2, 3, 4, 5]
        self.assertCannonicallyEqual([(1, 1, 1, 1, 1, 1, 1, 1, 1, 1), (1, 1, 1, 1, 1, 1, 1, 1, 2), (1, 1, 1, 1, 1, 1, 1, 3), (1, 1, 1, 1, 1, 1, 2, 2), (1, 1, 1, 1, 1, 1, 4), (1, 1, 1, 1, 1, 2, 3), (1, 1, 1, 1, 1, 5), (1, 1, 1, 1, 2, 2, 2), (1, 1, 1, 1, 2, 4), (1, 1, 1, 1, 3, 3), (1, 1, 1, 2, 2, 3), (1, 1, 1, 2, 5), (1, 1, 1, 3, 4), (1, 1, 2, 2, 2, 2), (1, 1, 2, 2, 4), (1, 1, 2, 3, 3), (1, 1, 3, 5), (1, 1, 4, 4), (1, 2, 2, 2, 3), (1, 2, 2, 5), (1, 2, 3, 4), (1, 3, 3, 3), (1, 4, 5), (2, 2, 2, 2, 2), (2, 2, 2, 4), (2, 2, 3, 3), (2, 3, 5), (2, 4, 4), (3, 3, 4), (5, 5)],
                                    make_change(bills,10))
    
    '''
    @weight(1)
    @number("2")
    def test_smart_change(self):
        bills2 = [1, 2, 5]
        bills3 = [1, 2, 5, 10]
        self.assertEqual(sorted(make_smart_change(bills2, 6, 1)), [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 2], [1, 1, 2, 2], [1, 5], [2, 2, 2]])
        self.assertEqual(sorted(make_smart_change(bills3, 16, 1)),[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2], [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 5], [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2], [1, 1, 1, 1, 1, 1, 1, 2, 2, 5], [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2], [1, 1, 1, 1, 1, 1, 5, 5], [1, 1, 1, 1, 1, 1, 10], [1, 1, 1, 1, 1, 2, 2, 2, 5], [1, 1, 1, 1, 2, 2, 2, 2, 2, 2], [1, 1, 1, 1, 2, 5, 5], [1, 1, 1, 1, 2, 10], [1, 1, 1, 2, 2, 2, 2, 5], [1, 1, 2, 2, 2, 2, 2, 2, 2], [1, 1, 2, 2, 5, 5], [1, 1, 2, 2, 10], [1, 2, 2, 2, 2, 2, 5], [1, 5, 5, 5], [1, 5, 10], [2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 5, 5], [2, 2, 2, 10]] )
    
    @weight(1)
    @number("3")
    def test_smart_change_limited(self):
        money = [(1, 3), (2, 3), (5, 1)]
        yourMoney2 =  [(1, 11), (2, 7), (5, 9), (10, 10), (20, 4)]
        self.assertEqual(sorted(make_smart_change_limited_bills(money, 6, 1)),[[1, 1, 2, 2], [1, 5], [2, 2, 2]])
        self.assertEqual(sorted(make_smart_change_limited_bills(yourMoney2, 16, 1)), [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2], [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 5], [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2], [1, 1, 1, 1, 1, 1, 1, 2, 2, 5], [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2], [1, 1, 1, 1, 1, 1, 5, 5], [1, 1, 1, 1, 1, 1, 10], [1, 1, 1, 1, 1, 2, 2, 2, 5], [1, 1, 1, 1, 2, 2, 2, 2, 2, 2], [1, 1, 1, 1, 2, 5, 5], [1, 1, 1, 1, 2, 10], [1, 1, 1, 2, 2, 2, 2, 5], [1, 1, 2, 2, 2, 2, 2, 2, 2], [1, 1, 2, 2, 5, 5], [1, 1, 2, 2, 10], [1, 2, 2, 2, 2, 2, 5], [1, 5, 5, 5], [1, 5, 10], [2, 2, 2, 5, 5], [2, 2, 2, 10]])
    '''

    @weight(1)
    @number("2")
    def test_smart_change_best_tests(self):
        """
        Testing Smart Change Best. The "First list" is the solution, the Second list is your computed output
        """
        money = [(1, 3), (2, 3), (5, 1)]
        yourMoney =  [(1, 11), (2, 7), (5, 9), (10, 10), (20, 4)]
        yourMoney2 =  [(1, 11), (2, 7), (5, 9), (10, 10), (20, 4)]

        def assertCannonicallyEqual(correct, student):
            self.assertEqual(sorted(correct), sorted(student))

        assertCannonicallyEqual([1,5], make_smart_change_best(money, 6, 1))
        assertCannonicallyEqual([1,5,10], make_smart_change_best(yourMoney, 16, 1))
        assertCannonicallyEqual([1], make_smart_change_best(yourMoney, 1, 1))
        assertCannonicallyEqual([2,2,5], make_smart_change_best([(1, 11), (2, 7), (5, 9), (10, 10), (20, 4)], 9,1))
    '''
    @weight(1)
    @number("5")
    def test_smart_change_memoized(self):
        money = [1, 2, 5]
        yourMoney =  [1, 2, 5, 10, 20]
        self.assertEqual(sorted(make_smart_change_memoized(money, 6, 1, memo={})), [1,5])
        self.assertEqual(sorted(make_smart_change_memoized(yourMoney, 296, 1, memo={})), [1, 5, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20])
        yourMoney =  [7, 59, 71, 97]
        self.assertEqual(sorted(make_smart_change_memoized(yourMoney, 1305, 1, memo={})), [7, 7, 7, 7, 59, 59, 59, 59, 71, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97])
        
    '''
    @weight(1)
    @number("3")
    def test_count_change(self):
        """
        Testing Count Change
        """
        money = [1, 2, 5]
        bills2 = [1, 2, 5, 10]
        yourMoney =  [7, 59, 71, 97]

        self.assertEqual(5, count_change(money, len(money), 6))
        self.assertEqual(25, count_change(bills2, len(bills2), 16))
        self.assertEqual(172, count_change(yourMoney, len(yourMoney), 1305))

if __name__ == "__main__":
    unittest.main()
                             