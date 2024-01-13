# AUTHOR: Francis Osei Annin
# DATE: 18/03/23
# DESCRIPTION: Singly Linked List
import math


class Node(object):
    def __init__(self):
        """initialise Node with value and pointer"""
        self.key = None
        self.pointer = None

    def get_node_value(self):
        """return node value"""
        return self.key

    def get_node_pointer(self):
        """return node pointer"""
        return self.pointer

    def set_node_value(self, new_node_value):
        """set a new node value"""
        self.key = new_node_value

    def set_node_pointer(self, new_node_pointer):
        """set new node pointer"""
        self.pointer = new_node_pointer


class SinglyLinkedList(object):

    def __init__(self):
        """initialise linked list with a head node"""
        self.head = None

    def find(self, node: Node):
        """"search for a node in the list"""
        current_node = self.head
        while current_node != node.key:
            current_node = node.pointer
            if match(current_node, node.key):
                break
            return True
        return False

    def remove(self, key):
        """"remove node in the list"""
        pass

    def traverse(self):
        """"move through items in the list"""

    def is_empty(self):
        """check if list is empty or not"""
        pass

    def append(self, node: Node):
        """add a new node to the end of list"""
        current_node = self.head
        while not current_node:
            if current_node is None:
                current_node = node
            else:
                current_node = current_node.pointer
        return current_node

    def prepend(self, node:Node):
        """add node to start of list"""
        new_node = node
        while self.head is not None:
            new_node.poi



def match(first_value, second_value):
    """"checks if two values in comparison match"""
    if math.isclose(first_value, second_value):
        return True
    return False
