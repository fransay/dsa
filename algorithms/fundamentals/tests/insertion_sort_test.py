import unittest
from algorithms.fundamentals.sort.insertion_sort import InsertionSort


class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        insertion_sort = InsertionSort([34, 54, 3, 5])
        result = insertion_sort.sort()
        expected = [3, 5, 34, 54]
        is_expected = True
        is_result = InsertionSort.compare(result, expected)
        self.assertEqual(is_expected, is_result)


