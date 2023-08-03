import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from conform import run_length_encode, run_length_decode


class TestCompression(unittest.TestCase):
    @weight(1)
    @number("5.1")
    def test_encode_1(self):
        message = 'BFFFFFBFFFF'
        encoded = run_length_encode(message)
        self.assertEqual(encoded, '1B5F1B4F')
    
    @weight(1)
    @number("5.2")
    def test_encode_2(self):
        message = 'BBBBB'
        encoded = run_length_encode(message)
        self.assertEqual(encoded, '5B')
    
    @weight(1)
    @number("5.3")
    def test_encode_3(self):
        message = 'BBFFBBBBBF'
        encoded = run_length_encode(message)
        self.assertEqual(encoded, '2B2F5B1F')
    
    @weight(1)
    @number("5.4")
    def test_encode_4(self):
        message = ''
        encoded = run_length_encode(message)
        self.assertEqual(encoded, '')
    
    @weight(1)
    @number("5.5")
    def test_encode_5(self):
        message = 'FBF'
        encoded = run_length_encode(message)
        self.assertEqual(encoded, '1F1B1F')
    
    @weight(1)
    @number("5.6")
    def test_encode_6(self):
        message = 'F'
        encoded = run_length_encode(message)
        self.assertEqual(encoded, '1F')
    
    @weight(1)
    @number("5.7")
    def test_decode_1(self):
        message = '1B5F1B4F'
        decoded = run_length_decode(message)
        self.assertEqual(decoded, 'BFFFFFBFFFF')
    
    @weight(1)
    @number("5.8")
    def test_decode_2(self):
        message = '5B'
        decoded = run_length_decode(message)
        self.assertEqual(decoded, 'BBBBB')
    
    @weight(1)
    @number("5.9")
    def test_decode_3(self):
        message = '2B2F5B1F'
        decoded = run_length_decode(message)
        self.assertEqual(decoded, 'BBFFBBBBBF')
    
    @weight(1)
    @number("5.10")
    def test_decode_4(self):
        message = ''
        decoded = run_length_decode(message)
        self.assertEqual(decoded, '')
    
    @weight(1)
    @number("5.11")
    def test_decode_5(self):
        message = '1F1B1F'
        decoded = run_length_decode(message)
        self.assertEqual(decoded, 'FBF')
    
    @weight(1)
    @number("5.12")
    def test_decode_6(self):
        message = '1F'
        decoded = run_length_decode(message)
        self.assertEqual(decoded, 'F')