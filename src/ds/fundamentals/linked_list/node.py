class Node(object):
    def __init__(self, key):
        """initialise node with value and pointers"""
        self.key = key
        self._left_pointer = None
        self._right_pointer = None

    def get_key(self):
        """return node value"""
        return self.key

    def get_left_pointer(self):
        """return left pointer"""
        return self._left_pointer

    def get_right_pointer(self):
        """return right pointer"""
        return self._right_pointer

    def set_left_pointer(self, new_left_pointer):
        """set new left pointer"""
        self._left_pointer = new_left_pointer

    def set__right_pointer(self, new_right_pointer):
        """set new right pointer"""
        self._right_pointer = new_right_pointer
