# AUTHOR: Francis Osei Annin
# DATE: 18/03/23
# DESCRIPTION: Linked List
# HISTORY: Invented by Allen Newell, Cliff Shaw and Herbert A. Simon in 1955-1956

class Node(object):
    def __init__(self):
        self._value = None
        self._pointer = None

    def get_node_value(self):
        """return node value"""
        return self._value

    def get_node_pointer(self):
        """return node pointer"""
        return self._pointer

    def set_node_value(self, new_node_value):
        """set a new node value"""
        self._value = new_node_value

    def set_node_pointer(self, new_node_pointer):
        """set new node pointer"""
        self._pointer = new_node_pointer


class LinkedList(object):
    pass
