
class SimpleQueue(object):
    """Simple Queue operates on the principle of first in first out"""
    def __init__(self):
        self.elements = []
        self.size = 0
        self.front = None
        self.rear = None
        self.last = None

    def enqueue(self, element):
        self.elements.append(element)
        self.size += 1
        self.last = self
        return self

    def dequeue(self):
        if self.size == 0:
            return None


# variables
# control-flow
# data types, i.e list, dict, set (inbuilt types)
# custom types -> class


class Person:
    # properties
    # methods - function
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.friends = []




