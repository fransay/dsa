class BinarySearch(object):
    """Binary Search"""

    def __init__(self, array):
        self.array = array
        self.size = len(self.array)

    def find(self, target_element):
        """search for target element in array using binary search approach"""
        low_index = 0
        high_index = (self.size - 1)
        while low_index <= high_index:
            mid_index = low_index + (high_index - low_index) // 2
            if target_element == self.array[mid_index]:
                return True
            elif target_element > self.array[mid_index]:
                low_index = mid_index + 1
            else:
                high_index = mid_index - 1
        return False

