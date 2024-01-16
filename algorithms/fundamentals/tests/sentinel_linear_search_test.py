import unittest

from ..search.sentinel_linear_search import SentinelLinearSearch


class TestSentinelLinearSearch(unittest.TestCase):
    """Test Sentinel Linear Search"""
    def test_sentinel_linear_search(self):
        test_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        sent_lin_search = SentinelLinearSearch(test_array)

        expected1 = sent_lin_search.find(20)
        result1 = False

        expected2 = True
        result2 = sent_lin_search.find(1)

        self.assertEqual(expected1, result1)
        # self.assertEqual(expected2, result2)
