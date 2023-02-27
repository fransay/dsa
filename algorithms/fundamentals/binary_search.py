"""
AUTHOR: Francis Osei Annin
DATE: 23/02/23
DESCRIPTION: This program searches for an element in a sequential data structure such 
an array/list using the binary search algorithm.
"""


"""
ALGORITHMS EXPALINED
* Given an array of n size and a target which represents a search element.
* A loop is set with a condition which breaks when the index of the first element
* is greater than or equal to the index of the last element.
* At each iteration, the array search space is divided into two with a if condition
* the algorithm returns a boolean and index value of the search result.
"""

def binary_search(array, target):
    """
    returns the a boolean representation and index values of target value 
    in a given array.
    Big Oh: Log(N)
    """
    low_index, high_index = 0, len(array) - 1
    while low_index <= high_index:
        mid_index = low_index + (high_index - low_index)//2
        if target == array[mid_index]:
            return True, mid_index
        elif target < array[mid_index]:
            high_index = mid_index - 1
        else:
            low_index = mid_index + 1
    return False, None

def main():
    print(binary_search([1,2,3,4,5,7],7))
    print(binary_search([7,8,9,10,11,12],10.00))

if __name__ == '__main__':
    main()
    

