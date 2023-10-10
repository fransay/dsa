# Author: Francis Osei Annin
# Date: 5/06/23
# Description: Binary search tree is not attributed to a single inventor,
# John Mauchly, Grace Hooper and Donald Knuth are key contributors.
# References: GPT 3.5

"""
<Binary Search Tree Explanation>
- A binary search tree (BST) is a specific type of binary tree. In a BST.
- In a BST each node has a value that is less than or equal to the root node
- the left subtree has nodes with value lesser than the root node.
- the right subtree has nodes with values greater than that of the root node.
- BSTs are designed for efficient searching,insertion a and deletion of elements


"""


class Node(object):
    """models a node in the tree"""

    def __init__(self, key):
        """init node key and left and right child pointers"""
        self.key = key
        self.right = None
        self.left = None


class BinarySearchTree(object):
    """
    A simple binary search tree that supports insertion,
    deletion, search, in-order traversal, pre-order traversal,
    post-order traversal, range queries including minimum and maximum
    node retrieval.
    """

    def __init__(self):
        """instantiate a new root node on object init"""
        self.root = Node(None)

    def search(self, target_key):
        """search for target_key in BST"""
        current_node = self.root
        while current_node.key != target_key and current_node.key is not None:
            if current_node.key == target_key:
                return current_node.key, True
            elif current_node > target_key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return current_node, False

    def insert(self, key):
        """insert node in BST"""
        current_node = self.root
        if current_node.key is None or current_node.key == key:
            current_node = Node(key)
            self.root = current_node
        if current_node.key is not None and current_node.key != key:
            if key < self.root.key:
                current_node = self.root.left
            elif key > self.root.key:
                current_node = self.root.right
        return current_node

    def get_minimum_key(self):
        """returns the node with the smallest key in BST"""
        current_node = self.root
        while current_node is not None:
            current_node = current_node.left
        return current_node.key

    def get_maximum_key(self):
        """returns the node with the largest key in the BST"""
        current_node = self.root
        while current_node is not None:
            current_node = current_node.right
        return current_node.key

    def inorder_traversal(self):
        """inorder traversal of BST"""
        pass

    def preorder_traversal(self):
        """postorder traversal of BST"""
        pass

    def remove(self, target_key):
        """remove the node with the same key as the argument named target_key"""
        pass
