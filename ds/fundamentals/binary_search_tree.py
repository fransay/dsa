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
    def __init__(self, value):
        """every node has a value, a pointer to right sub node and pointer to the left sub node"""
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree(object):
    """
    A simple binary search tree that supports insertion,
    deletion, search, in-order traversal, pre-order traversal,
    post-order traversal, range queries including minimum and maximum
    node retrieval.
    """
    pass



