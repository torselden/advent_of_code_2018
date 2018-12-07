import unittest
from day03 import day_3a, day_3b, parse_input
 
class Day02Test(unittest.TestCase):

    def setUp(self):
        pass

    def test_parse_input_return_correct_number_of_elements(self):
        self.assertEqual(1411,len(parse_input('3.txt')))

    def test_day03_a_example_test(self):
        input = ['#1 @ 1,3: 4x4','#2 @ 3,1: 4x4','#3 @ 5,5: 2x2']
        self.assertEqual(4,day_3a(input))

    def test_day03_b_example_test(self):
        pass