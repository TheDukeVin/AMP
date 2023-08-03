import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

import random

from ladder import all_ladders
from valid_word_list import get_valid_word_list
from ladder_solution import build_ladder_graph_solution, filter_word_list
from ladder_solution import randomly_generate_walk, is_ladder

class TestAllLadders(unittest.TestCase):
    @weight(1)
    @number("4.1")
    def test_1(self):
        """all_ladders- pit->cat, max_rungs=1"""
        w1="pit"
        w2="cat"
        max_rungs=1
        filtered_words = filter_word_list(get_valid_word_list(), len(w1))
        graph = build_ladder_graph_solution(filtered_words)
        actual = all_ladders(graph, w1, w2, get_valid_word_list(), max_rungs)
        expected = {('pit', 'pat', 'cat')}

        self.assertEqual(actual, expected)

    @weight(1)
    @number("4.2")
    def test_2(self):
        """all_ladders- pit->cat, max_rungs=2"""
        w1="pit"
        w2="cat"
        max_rungs=2
        filtered_words = filter_word_list(get_valid_word_list(), len(w1))
        graph = build_ladder_graph_solution(filtered_words)
        actual = all_ladders(graph, w1, w2, get_valid_word_list(), max_rungs)
        expected = {('pit', 'pat', 'oat', 'cat'), ('pit', 'put', 'cut', 'cat'), ('pit', 'pat', 'sat', 'cat'), 
                    ('pit', 'pat', 'hat', 'cat'), ('pit', 'sit', 'sat', 'cat'), ('pit', 'pat', 'vat', 'cat'), 
                    ('pit', 'pat', 'mat', 'cat'), ('pit', 'tit', 'tat', 'cat'), ('pit', 'pat', 'fat', 'cat'), 
                    ('pit', 'bit', 'bat', 'cat'), ('pit', 'pat', 'tat', 'cat'), ('pit', 'pat', 'bat', 'cat'), 
                    ('pit', 'pat', 'rat', 'cat'), ('pit', 'pat', 'eat', 'cat'), ('pit', 'pot', 'cot', 'cat'), 
                    ('pit', 'pet', 'pat', 'cat'), ('pit', 'hit', 'hat', 'cat'), ('pit', 'pot', 'pat', 'cat'), 
                    ('pit', 'put', 'pat', 'cat'), ('pit', 'pat', 'cat'), ('pit', 'fit', 'fat', 'cat')}

        self.assertEqual(actual, expected)

    @weight(1)
    @number("4.3")
    def test_3(self):
        """all_ladders- zoo->cat, max_rungs=2"""
        w1="zoo"
        w2="cat"
        max_rungs=2
        filtered_words = filter_word_list(get_valid_word_list(), len(w1))
        graph = build_ladder_graph_solution(filtered_words)
        actual = all_ladders(graph, w1, w2, get_valid_word_list(), max_rungs)
        expected = {('zoo', 'coo', 'cot', 'cat')}

        self.assertEqual(actual, expected)

    @weight(1)
    @number("4.4")
    def test_4(self):
        """all_ladders- zoo->cat, max_rungs=1"""
        w1="zoo"
        w2="cat"
        max_rungs=1
        filtered_words = filter_word_list(get_valid_word_list(), len(w1))
        graph = build_ladder_graph_solution(filtered_words)
        actual = all_ladders(graph, w1, w2, get_valid_word_list(),max_rungs)
        expected = set() #not possible with only 1 rung
        
        self.assertEqual(actual, expected)

    @weight(1)
    @number("4.5")
    def test_5(self):
        """all_ladders- zoo->cat, max_rungs=3"""
        w1="zoo"
        w2="cat"
        max_rungs=3
        filtered_words = filter_word_list(get_valid_word_list(), len(w1))
        graph = build_ladder_graph_solution(filtered_words)
        actual = all_ladders(graph, w1, w2, get_valid_word_list(),max_rungs)
        expected = {('zoo', 'too', 'tot', 'tat', 'cat'), ('zoo', 'coo', 'cot', 'cut', 'cat'), ('zoo', 'coo', 'cog', 'cot', 'cat'), 
                    ('zoo', 'too', 'coo', 'cot', 'cat'), ('zoo', 'coo', 'coy', 'cot', 'cat'), ('zoo', 'coo', 'cod', 'cot', 'cat'), 
                    ('zoo', 'coo', 'cot', 'cwt', 'cat'), ('zoo', 'moo', 'mao', 'mat', 'cat'), ('zoo', 'too', 'tot', 'cot', 'cat'), 
                    ('zoo', 'coo', 'cob', 'cab', 'cat'), ('zoo', 'goo', 'got', 'cot', 'cat'), ('zoo', 'coo', 'cot', 'cat'),
                    ('zoo', 'coo', 'con', 'cot', 'cat'), ('zoo', 'coo', 'cop', 'cap', 'cat'), ('zoo', 'moo', 'coo', 'cot', 'cat'), 
                    ('zoo', 'woo', 'coo', 'cot', 'cat'), ('zoo', 'goo', 'coo', 'cot', 'cat'), ('zoo', 'coo', 'cos', 'cot', 'cat'), 
                    ('zoo', 'coo', 'cow', 'caw', 'cat'), ('zoo', 'coo', 'cob', 'cot', 'cat'), ('zoo', 'coo', 'cop', 'cot', 'cat'), 
                    ('zoo', 'coo', 'cod', 'cad', 'cat'), ('zoo', 'coo', 'cow', 'cot', 'cat'), ('zoo', 'coo', 'con', 'can', 'cat'), 
                    ('zoo', 'boo', 'coo', 'cot', 'cat'), ('zoo', 'coo', 'cox', 'cot', 'cat')}
        
        self.assertEqual(actual, expected)

    @weight(1)
    @number("4.6")
    def test_6(self):
        """all_ladders- queue->smile, max_rungs=5"""
        w1="queue"
        w2="smile"
        max_rungs=3
        filtered_words = filter_word_list(get_valid_word_list(), len(w1))
        graph = build_ladder_graph_solution(filtered_words)
        actual = all_ladders(graph, w1, w2, get_valid_word_list(), max_rungs)
        expected = set() #not possible
        
        self.assertEqual(actual, expected)

    @weight(1)
    @number("4.7")
    def test_7(self):
        """all_ladders- fell->wilt, max_rungs=2"""
        w1="fell"
        w2="wilt"
        max_rungs=2
        filtered_words = filter_word_list(get_valid_word_list(), len(w1))
        graph = build_ladder_graph_solution(filtered_words)
        actual = all_ladders(graph, w1, w2, get_valid_word_list(), max_rungs)
        expected = {('fell', 'felt', 'welt', 'wilt'), ('fell', 'fill', 'will', 'wilt'), 
                    ('fell', 'well', 'welt', 'wilt'), ('fell', 'well', 'will', 'wilt')}

        self.assertEqual(actual, expected)

    @weight(1)
    @number("4.8")
    def test_8(self):
        """all_ladders- fell->wilt, max_rungs=3"""
        w1="fell"
        w2="wilt"
        max_rungs=3
        filtered_words = filter_word_list(get_valid_word_list(), len(w1))
        graph = build_ladder_graph_solution(filtered_words)
        actual = all_ladders(graph, w1, w2, get_valid_word_list(), max_rungs)
        expected = {('fell', 'cell', 'celt', 'welt', 'wilt'), ('fell', 'fill', 'till', 'tilt', 'wilt'), ('fell', 'fill', 'mill', 'milt', 'wilt'), 
                    ('fell', 'bell', 'well', 'will', 'wilt'), ('fell', 'fall', 'fill', 'will', 'wilt'), ('fell', 'felo', 'felt', 'welt', 'wilt'), 
                    ('fell', 'fill', 'dill', 'will', 'wilt'), ('fell', 'tell', 'well', 'welt', 'wilt'), ('fell', 'fill', 'sill', 'will', 'wilt'), 
                    ('fell', 'dell', 'dill', 'will', 'wilt'), ('fell', 'fill', 'jill', 'jilt', 'wilt'), ('fell', 'bell', 'belt', 'welt', 'wilt'), 
                    ('fell', 'fill', 'pill', 'will', 'wilt'), ('fell', 'felt', 'pelt', 'welt', 'wilt'), ('fell', 'sell', 'well', 'will', 'wilt'), 
                    ('fell', 'fill', 'bill', 'will', 'wilt'), ('fell', 'fill', 'jill', 'will', 'wilt'), ('fell', 'fill', 'will', 'wilt'), 
                    ('fell', 'tell', 'well', 'will', 'wilt'), ('fell', 'tell', 'till', 'will', 'wilt'), ('fell', 'fill', 'mill', 'will', 'wilt'), 
                    ('fell', 'fill', 'sill', 'silt', 'wilt'), ('fell', 'cell', 'well', 'welt', 'wilt'), ('fell', 'felt', 'belt', 'welt', 'wilt'), 
                    ('fell', 'sell', 'sill', 'will', 'wilt'), ('fell', 'well', 'weld', 'wild', 'wilt'), ('fell', 'fill', 'gill', 'will', 'wilt'), 
                    ('fell', 'well', 'wall', 'will', 'wilt'), ('fell', 'fill', 'kill', 'kilt', 'wilt'), ('fell', 'fill', 'will', 'wile', 'wilt'), 
                    ('fell', 'full', 'fill', 'will', 'wilt'), ('fell', 'dell', 'well', 'welt', 'wilt'), ('fell', 'felt', 'celt', 'welt', 'wilt'), 
                    ('fell', 'tell', 'till', 'tilt', 'wilt'), ('fell', 'well', 'welt', 'wilt'), ('fell', 'fill', 'will', 'wild', 'wilt'), 
                    ('fell', 'fill', 'hill', 'hilt', 'wilt'), ('fell', 'yell', 'well', 'welt', 'wilt'), ('fell', 'felt', 'melt', 'welt', 'wilt'), 
                    ('fell', 'felt', 'welt', 'wilt'), ('fell', 'sell', 'sill', 'silt', 'wilt'), ('fell', 'fill', 'gill', 'gilt', 'wilt'), 
                    ('fell', 'bell', 'well', 'welt', 'wilt'), ('fell', 'fill', 'will', 'wily', 'wilt'), ('fell', 'well', 'weld', 'welt', 'wilt'), 
                    ('fell', 'cell', 'well', 'will', 'wilt'), ('fell', 'fall', 'wall', 'will', 'wilt'), ('fell', 'fill', 'hill', 'will', 'wilt'), 
                    ('fell', 'fill', 'file', 'wile', 'wilt'), ('fell', 'felt', 'melt', 'milt', 'wilt'), ('fell', 'fill', 'kill', 'will', 'wilt'), 
                    ('fell', 'yell', 'well', 'will', 'wilt'), ('fell', 'well', 'will', 'wild', 'wilt'), ('fell', 'well', 'will', 'wile', 'wilt'), 
                    ('fell', 'well', 'will', 'wily', 'wilt'), ('fell', 'bell', 'bill', 'will', 'wilt'), ('fell', 'fill', 'till', 'will', 'wilt'),
                      ('fell', 'dell', 'well', 'will', 'wilt'), ('fell', 'sell', 'well', 'welt', 'wilt'), ('fell', 'well', 'will', 'wilt')}

        self.assertEqual(actual, expected)

    @weight(1)
    @number("4.9")
    def test_9(self):
        """all_ladders- show->cold, max_rungs=5"""
        w1="show"
        w2="cold"
        max_rungs=5
        filtered_words = filter_word_list(get_valid_word_list(), len(w1))
        graph = build_ladder_graph_solution(filtered_words)
        actual = all_ladders(graph, w1, w2, get_valid_word_list(), max_rungs)
        expected = {('show', 'shot', 'soot', 'moot', 'molt', 'colt', 'cold'), ('show', 'shot', 'soot', 'boot', 'bolt', 'colt', 'cold'), ('show', 'shot', 'soot', 'toot', 'coot', 'colt', 'cold'), 
                    ('show', 'slow', 'slot', 'soot', 'coot', 'colt', 'cold'), ('show', 'shot', 'soot', 'foot', 'food', 'fold', 'cold'), ('show', 'chow', 'chop', 'coop', 'coot', 'colt', 'cold'), 
                    ('show', 'shod', 'shot', 'soot', 'coot', 'colt', 'cold'), ('show', 'slow', 'slot', 'clot', 'coot', 'colt', 'cold'), ('show', 'shot', 'soot', 'hoot', 'coot', 'colt', 'cold'), 
                    ('show', 'shot', 'soot', 'foot', 'coot', 'colt', 'cold'), ('show', 'shot', 'soot', 'coot', 'colt', 'cold'), ('show', 'shot', 'soot', 'coot', 'cost', 'colt', 'cold'), 
                    ('show', 'shot', 'slot', 'soot', 'coot', 'colt', 'cold'), ('show', 'shot', 'slot', 'clot', 'coot', 'colt', 'cold'), ('show', 'shot', 'soot', 'coot', 'colt', 'cola', 'cold'), 
                    ('show', 'shop', 'chop', 'coop', 'coot', 'colt', 'cold'), ('show', 'shot', 'scot', 'soot', 'coot', 'colt', 'cold'), ('show', 'scow', 'scot', 'soot', 'coot', 'colt', 'cold'), 
                    ('show', 'shoe', 'shot', 'soot', 'coot', 'colt', 'cold'), ('show', 'shot', 'soot', 'loot', 'coot', 'colt', 'cold'), ('show', 'shot', 'soot', 'moot', 'coot', 'colt', 'cold'), 
                    ('show', 'shoo', 'shot', 'soot', 'coot', 'colt', 'cold'), ('show', 'shot', 'soot', 'coot', 'colt', 'cole', 'cold'), ('show', 'shot', 'soot', 'moot', 'mood', 'mold', 'cold'), 
                    ('show', 'shot', 'soot', 'coot', 'coat', 'colt', 'cold'), ('show', 'shot', 'soot', 'moot', 'molt', 'mold', 'cold'), ('show', 'shot', 'soot', 'coot', 'copt', 'colt', 'cold'), 
                    ('show', 'shot', 'soot', 'hoot', 'hood', 'hold', 'cold'), ('show', 'shot', 'soot', 'root', 'coot', 'colt', 'cold'), ('show', 'shot', 'soot', 'boot', 'coot', 'colt', 'cold'), 
                    ('show', 'shop', 'shot', 'soot', 'coot', 'colt', 'cold'), ('show', 'shot', 'spot', 'soot', 'coot', 'colt', 'cold'), ('show', 'shot', 'soot', 'boot', 'bolt', 'bold', 'cold')}

        self.assertEqual(actual, expected)


    @weight(1)
    @number("4.10")
    def test_10(self):
        """all_ladders- show->time, max_rungs=3"""
        w1="show"
        w2="time"
        max_rungs=3
        filtered_words = filter_word_list(get_valid_word_list(), len(w1))
        graph = build_ladder_graph_solution(filtered_words)
        actual = all_ladders(graph, w1, w2, get_valid_word_list(), max_rungs)
        expected = set() #not possible with only 1 rung
        
        self.assertEqual(actual, expected)

    # @weight(1)
    # @number("4.11")
    # def test_11(self):
    #     """all_ladders- randomly generated ladder is in all ladders."""
    #     words = filter_word_list(get_valid_word_list(), 4)
    #     graph = build_ladder_graph_solution(words)
    #     for _ in range(100):
    #         gen_ladder = randomly_generate_walk(4, words, graph)
    #         start = gen_ladder[0]
    #         end = gen_ladder[-1]
    #         if start != end and is_ladder(gen_ladder, start, end):
    #             print(start,"->", end)
    #             print("randomly generated ladder", gen_ladder)
    #             ladders = all_ladders(graph, start, end, words, max_rungs = len(gen_ladder)-2)
    #             self.assertIn(gen_ladder, ladders)

    # @weight(1)
    # @number("4.12")
    # def test_12(self):
    #     """all_ladders- all ladders are ladders."""
    #     words = filter_word_list(get_valid_word_list(), 4)
    #     graph = build_ladder_graph_solution(words)
    #     for _ in range(100):
    #        gen_ladder = randomly_generate_walk(4, words, graph)
    #        start = gen_ladder[0]
    #        end = gen_ladder[-1]
    #        if start != end:
    #            print(start,"->", end)
    #            for ladder in all_ladders(graph, start, end, words, max_rungs = len(gen_ladder)-2):
    #                print("checking your computed ladder", ladder)
    #                self.assert_(is_ladder(ladder, start, end))

if __name__ == "__main__":
    unittest.main()