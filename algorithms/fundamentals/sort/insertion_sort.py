class InsertionSort(object):
    """insertion sort"""

    def __init__(self, array):
        self.array = array

    def sort(self):
        """return a sorted array on the [self.array] property """
        length_of_array = len(self.array)
        current_index = 1
        while current_index < length_of_array:
            current_element = self.array[current_index]
            previous_index = current_index - 1
            while previous_index >= 0 and self.array[previous_index] > current_element:
                self.array[previous_index + 1] = self.array[previous_index]
                previous_index = previous_index - 1
            self.array[previous_index + 1] = current_element
            current_index = current_index + 1
        return self.array

    @staticmethod
    def compare(a, b):
        """compare two list items"""
        index = 0
        while index <= len(a) - 1 or index <= len(b) - 1:
            if a[index] != b[index]:
                return False
            index += 1
        return True
