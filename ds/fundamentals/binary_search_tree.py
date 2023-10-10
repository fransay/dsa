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
import setuptools


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
        self.root = None

    def search(self, target_key):
        """search for target_key in BST"""
        current_node = self.root
        while current_node is not None:
            if target_key == current_node.key:
                return current_node
            elif target_key < current_node.key:  # set current node to left node
                current_node = current_node.left
            else:
                current_node = current_node.right  # set current node to right node
        return None

    def insert(self, key):
        """insert node in BST"""

        new_node = Node(key)  # node of key to be inserted

        if not self.root:  # if self.root is empty/None, then insert the new node there
            self.root = new_node
            return

        current_node = self.root  # if root node is not empty
        while current_node:
            if key < current_node.key:
                if current_node.key:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    break
            elif key > current_node:
                if current_node:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break

    def delete(self, target_key):
        """delete node in BST"""
        pass

    def inorder(self):
        """inorder traversal of BST"""
        pass

    def preorder(self):
        """preorder traversal of BST"""
        pass

    def postorder(self):
        """postorder traversal of BST"""
        pass
