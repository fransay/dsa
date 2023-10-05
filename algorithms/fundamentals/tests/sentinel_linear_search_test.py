import unittest
from algorithms.fundamentals.search.sentinel_linear_search import sentinel_linear_search as sls


class SentinelLinearSearchTest(unittest.TestCase):
    """run all sentinel linear search test cases here"""

    def test_sentinel_linear_search(self):
        result_one = sls([1, 2, 4, 5], 4, 2)
        expected_one = (True, 1)
        self.assertEqual(result_one, expected_one)

        result_two = sls([1, 2, 4, 5], 4, 2)
        expected_two = (True, 1)
        self.assertEqual(result_two, expected_two)

        result_three = sls([11, 2, 4, 5], 4, 2)
        expected_three = (True, 1)
        self.assertEqual(result_three, expected_three)

        result_four = sls([1, 2, 4, 5], 4, 2)
        expected_four = (True, 1)
        self.assertEqual(result_four, expected_four)

        result_five = sls([1, 2, 4, 5], 4, 2)
        expected_five = (True, 1)
        self.assertEqual(result_five, expected_five)


