import unittest
from day06 import parse_input, parse_coordinates, calculate_finite_coords, calculate_largest_area, manhattan_dist
 
class Day06Test(unittest.TestCase):

    def test_parse_input_return_correct_number_of_elements(self):
        #Assert
        self.assertEqual(50, len(parse_input('6.txt')))

    def test_parse_coordinates_return_correct_list_of_coordinates(self):
        #Setup
        lines = ['1, 1', '1, 6', '8, 3', '3, 4', '5, 5', '8, 9']
        expected = [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)]
        #Test
        coords = parse_coordinates(lines)
        #Assert
        self.assertEqual(expected, coords)

    def test_calculate_finite_coords_return_correct_coords(self):
        # Arrange
        coords = [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)]
        expected = [(3, 4), (5, 5)]            
        #Test
        finite_coords = calculate_finite_coords(coords)
        #Assert
        self.assertEqual(expected, finite_coords)

    def test_manhattan_dist(self):
        #Setup
        finite_coord = (3, 4)
        A = (1, 1)
        B = (1, 6)
        C = (8, 3)
        D = (3, 4)
        E = (5, 5)
        F = (8, 9)
        #Test
        mh_A = manhattan_dist(A, finite_coord)
        mh_B = manhattan_dist(B, finite_coord)
        mh_C = manhattan_dist(C, finite_coord)
        mh_D = manhattan_dist(D, finite_coord)
        mh_E = manhattan_dist(E, finite_coord)
        mh_F = manhattan_dist(F, finite_coord)
        #Assert
        self.assertEqual(5, mh_A)
        self.assertEqual(4, mh_B)
        self.assertEqual(6, mh_C)
        self.assertEqual(0, mh_D)
        self.assertEqual(3, mh_E)
        self.assertEqual(10, mh_F)

    def test_calculate_largest_area(self):
        # Arrange
        coords = [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)]
        finite_coords = [(3, 4), (5, 5)]
        expected = 17            
        #Test
        finite_coords = calculate_finite_coords(coords)
        #Assert
        self.assertEqual(expected, calculate_largest_area(coords, finite_coords, 10))

    def test_day06_a_example_test(self):
        pass
    
    # def test_day06_b_example_test(self):
    #     input = 'dabAcCaCBAcCcaDA'
    #     result = remove_and_react(input)
    #     self.assertEqual(4, result)
        