# Author: Francis Osei Annin
# Date: 23/02/23
# Description: Linear Search

from math import isclose

"""
<Linear Search Algorithm Explanation> 
- Given a collection data structure, eg list, set, tuple etc.
- The algorithm walks through each item in the structure
- it checks each element in the data structure and compares it to the desired/target element.
- if found, it breaks and return a boolean and the position of the element in the structure.

<Edge Case>
- This naive implementation doesn't really work well for all data types.
- For example, a floating point number comparison of (0.5 + 0.1 != 0.6),
- this is as a result of the internal rounding precision of the floating point number. 
- In such an instance, the algorithm designed below won't be effective and efficient.
- see function **linear_search_float()**

<Extra Info>
- Linear search is one of the few fundamental search algorithm
- Implementation Difficulty: Easy
"""


def linear_search(array, target_element):
    """
    Accepts two parameters, array and target_element arguments
    returns a boolean and position(index) of the target element in the array/list.
    Big Oh: O(N)
    """
    for index, element in enumerate(array):
        if element == target_element:
            return True, index
    return False, None


# linear_search_float() tackles edge case defined on line 17
def linear_search_float(array, target_element: float):
    """
    **edge case**
    this implementation handles the edge case described on line 20 - 26
    Big oh: O(N)
    """
    for index, element in enumerate(array):
        if abs(element - target_element) < 1e-9:  # determines the absolute difference between the
            # target element and the element in array. if the difference is less than 
            # 1e-9 which is a very small number, then we can safely say,they are equal
            return True, index
        return False, None


# deploying isClose() from python Standard library to making linear search much better

def linear_search_upgrade(array, target_element):
    """
    returns a boolean representation and index of search element.
    linear_search_upgrade takes care of all numerical data types (int, float)
    Big Oh: O(N)
    """
    for index, element in enumerate(array):
        if isclose(element, target_element):
            return True, index
    return False, None

# uncomment lines 71-76 in case you wish to run this as a script
# either than that, all unit tests relating to linear search can
# be found at algorithms/fundamentals/search/tests or a relative path
# of ../test

# if __name__ == '__main__':
#     print(linear_search([1, 2, 3, 4, 5, 6, 7], 2))
#     print(linear_search(["male", "female"], "male"))
#     print(linear_search(["male", "female"], "mango"))
#     print(linear_search([100, 34.45, 3.00], 3))
#     print(linear_search_upgrade([1, 2, 3, 4, 5, 6, 7], 2))
