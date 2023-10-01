# Author: Francis Osei Annin
# Date: 23/02/23
# Description: Binary Search
# History: Invented by A.K Chandra in 1971 at Standford


"""
<Binary Search Algorithm Explanation>
- Given a collection data structure, e.g. list, set, tuples etc.
- The BSA (Binary Search Algorithm) iteratively divides the search space into two.
- And for each search space of the collection data structure, the value of the middle index is determined
- In a case where the target value or element is equal to the middle index value of the search space, the iteration breaks.
- The position and value of the middle value equal to the target element is returned.

<Edge Case>
- No peculiar edge case.
- When comparing values between the target element those in the element search space,
- Note floating point comparison should be treated with much care as can be seen in linear_search.py

<Extra Info>
- Kindly note this algorithm only works validly for sorted collection data structures.
"""


def binary_search(array, target):
    """
    returns the boolean and index representations of target value in a given array.
    Big O: log(N)
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

# uncomment lines 46-51 in case you wish to run this as a script
# either than that, all unit tests relating to linear search can
# be found at algorithms/fundamentals/search/tests or a relative path
# of ../test

# def main():
#     print(binary_search([1, 2, 3, 4, 5, 7], 7))
#     print(binary_search([7, 8, 9, 10, 11, 12], 10.00))
#
# if __name__ == '__main__':
#     main()
