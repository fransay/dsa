# Author: Francis Osei Annin
# Date: 23/02/23
# Description: Binary Search
# History: Invented by A.K Chandra in 1971 at Standford

"""
ALGORITHMS EXPLAINED
* Given an array of n size and a target which represents a search element.
* A loop is set with a condition which breaks when the index of the first element
* is greater than or equal to the index of the last element.
* At each iteration, the array search space is divided into two with if condition
* the algorithm returns a boolean and index value of the search result.

EDGE CASE
* floating point comparison must be taken care. See linear_search.py script for
extended information on handling floating point comparison.
"""


def binary_search(array, target):
    """
    returns the boolean representation and index values of target value
    in a given array.
    Big Oh: log(N)
    """
    low_index, high_index = 0, len(array) - 1
    while low_index <= high_index:
        mid_index = low_index + (high_index - low_index) // 2
        if target == array[mid_index]:
            return True, mid_index
        elif target < array[mid_index]:
            high_index = mid_index - 1
        else:
            low_index = mid_index + 1
    return False, None


def main():
    print(binary_search([1, 2, 3, 4, 5, 7], 7))
    print(binary_search([7, 8, 9, 10, 11, 12], 10.00))


if __name__ == '__main__':
    main()
