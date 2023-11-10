# AUTHOR: Francis Osei Annin
# DATE: 18/03/23
# DESCRIPTION: Singly Linked List

class Node(object):
    def __init__(self):
        """initialise Node with value and pointer"""
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


class SinglyLinkedList(object):

    def __init__(self):
        """initialise linked list with a head node"""
        self.head = None

    def insert(self, key):
        """insert node into linked list"""
        new_node = Node()

        if self.head is None:  # check if head is empty
            self.head = new_node
            self.head.set_node_value(key)

        # if self.head not empty, check pointer and see if that is not empty as well.
        # if it is empty, create a new node and link


