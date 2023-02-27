"""
AUTHOR: Francis Osei Annin
DATE: 23/02/23
DESCRIPTION: This program searches for an element in a sequential data structure such 
an array/list using the binary search algorithm.
"""


# TIME AND SPACE COMPLEXITY
# Big Oh: log(N)

def binary_search(array, target):
    """
    returns the a boolean representation and index values of target value 
    in a given array.
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
    

