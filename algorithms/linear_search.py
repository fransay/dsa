
"""
AUTHOR: Francis Osei Annin
DATE: 23/02/23
DESCRIPTION: This program searches for an element in a sequential data structure such 
as an array/list.
"""



"""
TIME AND SPACE COMPLEXITY
-------------------------
Big OH: O(n)

"""
def linear_search(array, target_element):
    """
    This function accepts two parameters, array and target_element arguments
    returns a boolean and position(index) of the target element in the array/list.
    """
    for index, element in enumerate(array):
        if element == target_element:
            return True, index
    return False, None


if __name__ == '__main__':
    print(linear_search([1,2,3,4,5,6,7], 2))
    print(linear_search(["male", "female"], "male"))
    print(linear_search(["male", "female"], "female"))
    print(linear_search([100,34.45, 3.00], 3))
    
    
