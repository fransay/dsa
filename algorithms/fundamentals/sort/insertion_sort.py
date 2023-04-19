# AUTHOR: Francis Osei Annin
# DATE: 11/04/23
# DESCRIPTION: A program that sort elements in a collection using the insertion sort method.
# HISTORY: Invented in 1946 by John Mauchly.

"""
ALGORITHM EXPLAINED
Insertion sort is a simple yet thought-provoking algorithm.
* The algorithm takes and unsorted array of order-able elements
* It further goes ahead to create a sorted space in the same array
* by setting a pointer to an arbitrary index value, normally 1
* an iterative comparison is made between the current element the previous
* if the previous element is greater than the current, a swap is performed
* else the structure stays the same and the index of the current element is
* promoted by one and the current element is set to the new current which
* described by the previous_index + 1.
"""


def insertion_sort(array: list):
    """
    accepts an unsorted array as input and returns a new sorted version.
    BIG O: O(N^2)
    """
    length_of_array = len(array)  # determine the length of the array
    current_index = 1  # set index of current element to 1
    while current_index < length_of_array:
        current_element = array[current_index]  # current element
        previous_index = current_index - 1  # index of previous element
        while previous_index >= 0 and array[previous_index] > current_element:
            array[previous_index + 1] = array[previous_index]  # previous element is promoted to the next index
            previous_index = previous_index - 1  # previous_index is shifted backwards by one
        array[previous_index + 1] = current_element
        current_index = current_index + 1  # increase index of current element by one
    return array


if __name__ == '__main__':
    print(insertion_sort([1, 31, 4]))
    print(insertion_sort([2, 4, 1, 0, 5]))
