# AUTHOR: Francis Osei Annin
# DATE: 17/02/23
# DESCRIPTION: This program linearly searches for desired elements in a collection data structure,
# using the sentinel approach.


"""
ALGORITHM EXPLAINED

The
"""


# sentinel_ls: sentinel_ls is an abbreviation of the term sentinel linear search
def sentinel_ls(array, n, key):
    """
    returns a boolean representation of an index value of the key in search
    array: array structure
    n: size of the array
    key: item in search
    """
    last_element = array[n - 1]
    array[n - 1] = key
    counter = 0
    while array[counter] != key:
        counter += 1
    array[n - 1] = last_element
    if counter < n - 1 or counter == key:
        return True, counter
    return False, counter


if __name__ == '__main__':
    print(sentinel_ls([1, 2, 4, 5], 4, 2))
