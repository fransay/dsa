# Author: Francis Osei Annin
# Date: 01/10/23
# Description: Binary Search Unit Tests

import unittest
import algorithms.fundamentals.search.binary_search as bs


class BinarySearchTest(unittest.TestCase):
    """run all binary search test cases here"""
    def test_binary_search(self):
        """binary search unitest"""
        program_output_one = bs.binary_search([1, 2, 3, 4, 5, 7], 7)
        expected_output_one = (True, 5)
        self.assertEqual(program_output_one, expected_output_one)

        program_output_two = bs.binary_search([7, 8, 9, 10, 11, 12], 100.00)
        expected_output_two = (False, None)
        self.assertEqual(program_output_two, expected_output_two)