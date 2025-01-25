# AUTHOR: Francis Osei Annin
# DATE: 18/03/23
# DESCRIPTION: Singly Linked List
import math
from node import Node


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

    def traverse(self):
        """"move through items in the list and display them in an inbuilt list"""
        disp_list = []
        current_node: Node = self.head
        while current_node is not None:
            disp_list.append(current_node.key)
            current_node = current_node.pointer
        return disp_list

    def is_empty(self):
        """check if list is empty or not"""
        if self.head is None:
            return True
        return False

    def append(self, node: Node):
        """add a new node to the end of list"""
        current_node = self.head
        while not current_node:
            if current_node is None:
                current_node = node
            else:
                current_node = current_node.pointer
        return current_node

    def prepend(self, node: Node):
        """add node to start of list"""
        new_node = node
        while self.head is not None:
            new_node.pointer = self.head
            self.head = new_node
        return

    def remove(self, key):
        """"remove node in the list"""
        pass


def match(first_value, second_value):
    """"checks if two values in comparison match"""
    if math.isclose(first_value, second_value):
        return True
    return False


def key_2_node(key):
    """returns node object of key"""
    return Node(key)
