# Author: Francis Osei Annin
# Date: 14/04/23
# Description: A stack data structure

class Stack(object):
    """A stack is a data structure, that follows the last in, first out principle."""

    def __init__(self):
        """initialise stack with empty element list"""
        self.elements = []

    def push(self, key):
        """add key to the top of the stack"""
        self.elements.append(key)

    def pop(self):
        """remove first element of stack"""
        if not self.is_empty():
            return self.elements.pop()
        else:
            return Exception("Can't pop from empty stack")

    def peek(self):
        """return the first element on stack"""
        if not self.is_empty():
            return self.elements[-1]
        else:
            return Exception("Can't peek on empty stack")

    def size(self):
        """return the size of the stack"""
        return len(self.elements)

    def is_empty(self):
        """return boolean if size is empty or not"""
        return self.elements == 0

    def sweet_pop(self):
        """reduce the top element of the stack"""
        if not self.is_empty():
            del self.elements[-1]
        else:
            return Exception("Underflow Error, can't peek on empty stack")


