
class Node(object):
    def __init__(self, key):
        """initialise Node with value and pointer"""
        self.key = key
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