import unittest
import random
from gradescope_utils.autograder_utils.decorators import weight, number

from detectives import detect

class TestDetection(unittest.TestCase):
    @weight(1)
    @number("1")
    def test_trivial(self):
        """Trivial cases hold"""
        tests = [[0] * i for i in range(10)]
        for sequence in tests:
            self.assertEqual(True, detect(sequence))
    
    @weight(1)
    @number("2")
    def test_KN(self):
        """Recognizes K_n"""
        evens = [[1,1], [2,2,2], [3,3,3,3]]
        for sequence in evens:
            self.assertEqual(True, detect(sequence))
    
    @weight(1)
    @number("3")
    def test_oddball(self):
        """Detects oddball liars"""
        for i in range(1000):
            odds = [ random.randint(0,i) for i in range(10)]
            if sum(odds) % 2 == 0:
                self.assertEqual(False, detect(odds+[1]))
            else:
                self.assertEqual(False, detect(odds))
                             
    @weight(1)
    @number("4")
    def test_random(self):
        """Passes randomly generated non-liars"""
        n=10
        nodes = list(range(n))
        edges = [(i,j) for i in range(n) for j in range(n) if i != j]
        for i in range(1000):
            num_edges = random.randint(1,len(edges))
            edge_sample = random.sample(edges, num_edges)
            adj = {i:set() for i in nodes}
            for (i,j) in edge_sample:
                adj[i].add(j)
                adj[j].add(i)
            sequence = [len(adj[i]) for i in nodes]
            self.assertEqual(True, detect(sequence))

                                 
    @weight(1)
    @number("5")
    def test_random(self):
        """Fails random single liars"""
        n=10
        nodes = list(range(n))
        edges = [(i,j) for i in range(n) for j in range(n) if i != j]
        for i in range(1000):
            num_edges = random.randint(1,len(edges))
            edge_sample = random.sample(edges, num_edges)
            adj = {i:set() for i in nodes}
            for (i,j) in edge_sample:
                adj[i].add(j)
                adj[j].add(i)
            sequence = [len(adj[i]) for i in nodes]
            chaosidx = random.randint(0,len(sequence)-1)
            sequence[chaosidx] = sequence[chaosidx] + 1
            self.assertEqual(False, detect(sequence))

    @weight(1)
    @number("6")
    def test_KN(self):
        """Fails Non-Obvious Cases"""
        for _ in range(99):
            sequence = [100] + [ random.randint(0,49) * 2 for j in range(99)]
            self.assertEqual(False, detect(sequence)) 
  

if __name__ == "__main__":
    unittest.main()
