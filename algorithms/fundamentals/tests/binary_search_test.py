import unittest
from ..search.binary_search import BinarySearch


class TestBinarySearch(unittest.TestCase):
    """Test Binary Search"""

    def test_find(self):
        """test find method"""
        test_array = [1, 2, 3, 4]
        bin_search = BinarySearch(test_array)

        result1 = bin_search.find(3)  # expect true
        expected1 = True

        result2 = bin_search.find(22)  # expect false
        expected2 = False

        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
