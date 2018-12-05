import unittest
from day05 import *
 
class Day05Test(unittest.TestCase):

    def test_parse_input_return_correct_number_of_elements(self):
        self.assertEqual(50000,len(parse_input('5.txt')))

    def test_day05_a_example_test(self):
        input = 'dabAcCaCBAcCcaDA'
        self.assertEqual((10,['d', 'a', 'b', 'C', 'B', 'A', 'c', 'a', 'D', 'A']),react(input))
    
    def test_day05_b_example_test(self):
        input = 'dabAcCaCBAcCcaDA'
        result = remove_and_react(input)
        self.assertEqual(4,result)
        