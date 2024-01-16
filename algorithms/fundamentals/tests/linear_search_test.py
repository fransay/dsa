import unittest
from ..search.linear_search import LinearSearch


class TestBinarySearch(unittest.TestCase):
    """Test Binary Search"""

    def test_find(self):
        """test find method"""
        test_array = [1, 2, 3, 4]
        lin_search = LinearSearch(test_array)

        result1 = lin_search.find(0)  # expect false
        expected1 = False

        result2 = lin_search.find(1)  # expect true
        expected2 = True

        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)

