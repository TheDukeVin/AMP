import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

from ladder import build_ladder_graph

from valid_word_list import get_valid_word_list
from ladder_solution import build_ladder_graph_solution, filter_word_list
from ladder_solution import get_letter_masks as get_letter_masks_solution

class TestBuildLadderGraph(unittest.TestCase):
    @weight(1)
    @number("2.1")
    def test_1(self):
        """build_ladder_graph- 3 letter words from get_valid_word_list"""
        words_3_letters = filter_word_list(get_valid_word_list(), 3)
        expected = build_ladder_graph_solution(words_3_letters)
        actual = build_ladder_graph(words_3_letters)
        
        self.assertEqual(expected, actual)


    @weight(1)
    @number("2.2")
    def test_2(self):
        """build_ladder_graph- 4 letter words from get_valid_word_list"""
        words_4_letters = filter_word_list(get_valid_word_list(), 4)
        expected = build_ladder_graph_solution(words_4_letters)
        actual = build_ladder_graph(words_4_letters)
        
        self.assertEqual(expected, actual)

    @weight(1)
    @number("2.3")
    def test_3(self):
        """build_ladder_graph- 5 letter words from get_valid_word_list"""
        words_5_letters = filter_word_list(get_valid_word_list(), 5)
        expected = build_ladder_graph_solution(words_5_letters)
        actual = build_ladder_graph(words_5_letters)
        
        self.assertEqual(expected, actual)

    @weight(1)
    @number("2.4")
    def test_4(self):
        """build_ladder_graph- 6 letter words from get_valid_word_list"""
        words_6_letters = filter_word_list(get_valid_word_list(), 6)
        expected = build_ladder_graph_solution(words_6_letters)
        actual = build_ladder_graph(words_6_letters)
        self.assertEqual(expected, actual)

    @weight(1)
    @number("2.5")
    def test_5(self):
        """build_ladder_graph- 7 letter words from get_valid_word_list"""
        words_7_letters = filter_word_list(get_valid_word_list(), 7)
        expected = build_ladder_graph_solution(words_7_letters)
        actual = build_ladder_graph(words_7_letters)
        
        self.assertEqual(expected, actual)

    # @weight(1)
    # @number("2.6")
    # def test_6(self):
    #   """build_ladder_graph- a words masks intersect with its neighbors"""
    #    words_5_letters = filter_word_list(get_valid_word_list(), 5)
    #    graph = build_ladder_graph(words_5_letters)
    #    for word in words_5_letters:
    #        for mask in get_letter_masks_solution(word):
    #            for neighbor in graph[mask]:
    #                print("Original word:", word, "Neighbor:", neighbor)
    #                self.assertIn(mask, get_letter_masks_solution(neighbor))

    # @weight(1)
    # @number("2.7")
    # def test_7(self):
    #    """build_ladder_graph- words that differ by one letter are in each others adjacency list"""
    #    words_4_letters = filter_word_list(get_valid_word_list(), 4)
    #    graph = build_ladder_graph(words_4_letters)
    #    for word in words_4_letters:
    #        for other_word in words_4_letters:
    #            for mask in get_letter_masks_solution(word):
    #                if mask in get_letter_masks_solution(other_word):
    #                    print("original word:", word, "other word:", other_word)
    #                    self.assertIn(word, graph[mask])
    #                    self.assertIn(other_word, graph[mask])

if __name__ == "__main__":
    unittest.main()