from math import isclose


class LinearSearch(object):
    """Linear Search"""

    def __init__(self, array):
        self.array = array

    def find(self, target_element):
        """search for target element in array using linear search"""
        for element_in_array in self.array:
            if LinearSearch.compare(element_in_array, target_element):
                return True
        return False

    @staticmethod
    def compare(obj1, obj2):
        """return true if two objs are very close and false otherwise"""
        closeness = isclose(obj1, obj2)
        return closeness
