import unittest
from day04 import day_4a, day_4b, parse_input, parse_lines
 
class Day02Test(unittest.TestCase):

    def setUp(self):
        pass

    # def test_parse_input_return_correct_number_of_elements(self):
    #     self.assertEqual(20,len(parse_lines('4.txt')))

    def test_day04_a_example_test(self):
        input = ['[1518-11-01 00:00] Guard #10 begins shift','[1518-11-01 00:05] falls asleep','[1518-11-01 00:25] wakes up','[1518-11-01 00:30] falls asleep','[1518-11-01 00:55] wakes up','[1518-11-01 23:58] Guard #99 begins shift','[1518-11-02 00:40] falls asleep','[1518-11-02 00:50] wakes up','[1518-11-03 00:05] Guard #10 begins shift','[1518-11-03 00:24] falls asleep','[1518-11-03 00:29] wakes up','[1518-11-04 00:02] Guard #99 begins shift','[1518-11-04 00:36] falls asleep','[1518-11-04 00:46] wakes up','[1518-11-05 00:03] Guard #99 begins shift','[1518-11-05 00:45] falls asleep','[1518-11-05 00:55] wakes up]']
        self.assertEqual(240,day_4a())

    # def test_day04_b_example_test(self):
    #     pass
