# Author: Francis Osei Annin
# Date: 01/10/23
# Description: Linear Search Unit Tests

import unittest
import algorithms.fundamentals.search.linear_search as ls


class LinearSearchTest(unittest.TestCase):
    """run all linear search unit tests here"""

    def test_linear_search(self):
        program_outcome_test_one = ls.linear_search([1, 2, 3, 4, 5, 6, 7], 2)
        expected_outcome_test_one = (True, 1)
        self.assertEqual(program_outcome_test_one, expected_outcome_test_one)

        program_outcome_test_two = ls.linear_search(["male", "female"], "male")
        expected_outcome_test_two = (True, 0)
        self.assertEqual(program_outcome_test_two, expected_outcome_test_two)

        program_outcome_test_three = ls.linear_search(["male", "female"], "female")
        expected_outcome_test_three = (True, 1)
        self.assertEqual(program_outcome_test_three, expected_outcome_test_three)

        program_outcome_test_four = ls.linear_search(["male", "female"], "mango")
        expected_outcome_test_four = (False, None)
        self.assertEqual(program_outcome_test_four, expected_outcome_test_four)

        program_outcome_test_five = ls.linear_search([1, 2, 3, 4, 5, 65, 10, 7, 8, 6], 10)
        expected_outcome_test_five = (True, 6)
        self.assertEqual(program_outcome_test_five, expected_outcome_test_five)

    def test_linear_search_float(self):
        pass

    def linear_search_upgrade(self):
        pass
