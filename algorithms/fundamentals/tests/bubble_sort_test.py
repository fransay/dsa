import unittest

from algorithms.fundamentals.sort.bubble_sort import BubbleSort


class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        array = [23, 3, 5, 2, 31, 4]
        bubble_sort = BubbleSort(array)
        observed_bubble_sort = bubble_sort.sort()
        expected_bubble_sort = [2, 3, 4, 5, 23, 31]
        self.assertEqual(observed_bubble_sort, expected_bubble_sort)
