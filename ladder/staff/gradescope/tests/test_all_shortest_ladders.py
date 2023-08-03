import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

import random

from ladder import all_shortest_ladders

from valid_word_list import get_valid_word_list
from ladder_solution import build_ladder_graph_solution, filter_word_list
from ladder_solution import get_letter_masks as get_letter_masks_solution
from ladder_solution import is_ladder, randomly_generate_walk

class TestAllShortestLadders(unittest.TestCase):
    @weight(1)
    @number("3.1")
    def test_1(self):
        """all_shortest_ladders- PIT -> CAT"""
       
        w1="PIT"
        w2="CAT"
        words_3_letters = filter_word_list(get_valid_word_list(), 3)
        graph = build_ladder_graph_solution(words_3_letters)
        actual = all_shortest_ladders(graph, w1, w2, get_valid_word_list())
        expected = {('pit', 'pat', 'cat')}

        self.assertEqual(actual, expected)

    @weight(1)
    @number("3.2")
    def test_2(self):
        """all_shortest_ladders- pit -> CAT"""
       
        w1="pit"
        w2="CAT"
        words_3_letters = filter_word_list(get_valid_word_list(), 3)
        graph = build_ladder_graph_solution(words_3_letters)
        actual = all_shortest_ladders(graph, w1, w2, get_valid_word_list())
        expected = {('pit', 'pat', 'cat')}

        self.assertEqual(actual, expected)

    @weight(1)
    @number("3.3")
    def test_3(self):
        """all_shortest_ladders- ate -> cat"""
       
        w1="ate"
        w2="cat"
        words_3_letters = filter_word_list(get_valid_word_list(), 3)
        graph = build_ladder_graph_solution(words_3_letters)
        actual = all_shortest_ladders(graph, w1, w2, get_valid_word_list())
        expected = {('ate', 'ape', 'apt', 'opt', 'oat', 'cat')}

        self.assertEqual(actual, expected)

    @weight(1)
    @number("3.4")
    def test_4(self):
        """all_shortest_ladders- kite -> BEST"""
       
        w1="kite"
        w2="BEST"
        words_4_letters = filter_word_list(get_valid_word_list(), 4)
        graph = build_ladder_graph_solution(words_4_letters)
        actual = all_shortest_ladders(graph, w1, w2, get_valid_word_list())
        expected = {('kite', 'kits', 'bits', 'bets', 'bess', 'best'), 
                    ('kite', 'bite', 'bate', 'base', 'bast', 'best'), 
                    ('kite', 'kate', 'bate', 'base', 'bast', 'best'), 
                    ('kite', 'bite', 'bits', 'bets', 'bess', 'best')}

        self.assertEqual(actual, expected)

    @weight(1)
    @number("3.5")
    def test_5(self):
        """all_shortest_ladders- kite -> kilt"""
       
        w1="kite"
        w2="kilt"
        words_4_letters = filter_word_list(get_valid_word_list(), 4)
        graph = build_ladder_graph_solution(words_4_letters)
        actual = all_shortest_ladders(graph, w1, w2, get_valid_word_list())
        expected = {('kite', 'mite', 'mile', 'milt', 'kilt'), 
                    ('kite', 'mite', 'mitt', 'milt', 'kilt')}

        self.assertEqual(actual, expected)

    @weight(1)
    @number("3.6")
    def test_6(self):
        """all_shortest_ladders- show -> cold"""
       
        w1="show"
        w2="cold"
        words_4_letters = filter_word_list(get_valid_word_list(), 4)
        graph = build_ladder_graph_solution(words_4_letters)
        actual = all_shortest_ladders(graph, w1, w2, get_valid_word_list())
        expected = {('show', 'shot', 'soot', 'coot', 'colt', 'cold')}

        self.assertEqual(actual, expected)

    @weight(1)
    @number("3.7")
    def test_7(self):
        """all_shortest_ladders- mossy -> house"""
       
        w1="mossy"
        w2="house"
        words_5_letters = filter_word_list(get_valid_word_list(), 5)
        graph = build_ladder_graph_solution(words_5_letters)
        actual = all_shortest_ladders(graph, w1, w2, get_valid_word_list())
        expected = {('mossy', 'mousy', 'mouse', 'house')}

        self.assertEqual(actual, expected)

    @weight(1)
    @number("3.8")
    def test_8(self):
        """all_shortest_ladders- mathy -> house"""
       
        w1="mathy"
        w2="house"
        words_5_letters = filter_word_list(get_valid_word_list(), 5)
        graph = build_ladder_graph_solution(words_5_letters)
        actual = all_shortest_ladders(graph, w1, w2, get_valid_word_list())
        expected = set()

        self.assertEqual(actual, expected)

    @weight(1)
    @number("3.9")
    def test_9(self):
        """all_shortest_ladders- windy -> water"""
       
        w1="windy"
        w2="water"
        words_5_letters = filter_word_list(get_valid_word_list(), 5)
        graph = build_ladder_graph_solution(words_5_letters)
        actual = all_shortest_ladders(graph, w1, w2, get_valid_word_list())
        expected = {('windy', 'winds', 'wands', 'wanes', 'waves', 'waver', 'water'), 
                    ('windy', 'winds', 'wines', 'wives', 'waves', 'waver', 'water'), 
                    ('windy', 'winds', 'wands', 'wanes', 'wages', 'wager', 'water'), 
                    ('windy', 'winds', 'wands', 'wanes', 'wades', 'wader', 'water'), 
                    ('windy', 'winds', 'wines', 'wanes', 'waves', 'waver', 'water'), 
                    ('windy', 'winds', 'wines', 'wanes', 'wades', 'wader', 'water'), 
                    ('windy', 'winds', 'wines', 'wanes', 'wages', 'wager', 'water')}

        self.assertEqual(actual, expected)

    @weight(1)
    @number("3.10")
    def test_10(self):
        """all_shortest_ladders- show -> time"""
       
        w1="show"
        w2="time"
        words_4_letters = filter_word_list(get_valid_word_list(), 4)
        graph = build_ladder_graph_solution(words_4_letters)
        actual = all_shortest_ladders(graph, w1, w2, get_valid_word_list())
        expected = set()  #shortest path > 5 rungs: ['show', 'shot', 'soot', 'toot', 'tort', 'tore', 'tire', 'time']

        self.assertEqual(actual, expected)

    @weight(1)
    @number("3.11")
    def test_11(self):
        """all_shortest_ladders- show -> show"""
       
        w1="show"
        w2="show"
        words_4_letters = filter_word_list(get_valid_word_list(), 4)
        graph = build_ladder_graph_solution(words_4_letters)
        actual = all_shortest_ladders(graph, w1, w2, get_valid_word_list())
        expected = set()  #shortest path > 5 rungs: ['show', 'shot', 'soot', 'toot', 'tort', 'tore', 'tire', 'time']
        self.assertEqual(actual, expected)

    # @weight(1)
    # @number("3.11")
    # def test_11(self):
    #     """all_shortest_ladders- all_shortest_ladders aren't longer than randomly generated ladders"""
    #     words = filter_word_list(get_valid_word_list(), 4)
    #     graph = build_ladder_graph_solution(words)
    #     for _ in range(100):
    #         gen_ladder = randomly_generate_walk(4, words, graph)
    #         start = gen_ladder[0]
    #         end = gen_ladder[-1]
    #         print(start,"->", end)
    #         print(gen_ladder)
    #         for short_ladder in all_shortest_ladders(graph, start, end, words):
    #             print(short_ladder)
    #             self.assertGreaterEqual(6, len(short_ladder))
    #             for word in short_ladder:
    #                 self.assertIn(word, words)

    # @weight(1)
    # @number("3.12")
    # def test_12(self):
    #     """all_shortest_ladders- all_shortest_ladders are ladders"""
    #     words = filter_word_list(get_valid_word_list(), 4)
    #     graph = build_ladder_graph_solution(words)
    #     for _ in range(100):
    #         gen_ladder = randomly_generate_walk(4, words, graph)
    #         start = gen_ladder[0]
    #         end = gen_ladder[-1]
    #         print(start,"->", end)
    #         print(gen_ladder)
    #         for short_ladder in all_shortest_ladders(graph, start, end, words):
    #             self.assert_(is_ladder(short_ladder, start, end))

if __name__ == "__main__":
    unittest.main(verbosity=4)
                

