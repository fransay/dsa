# Author: Francis Osei Annin
# Date: 5/10/23
# Description: Test Binary Search Tree

import unittest
from ds.fundamentals.binary_search_tree import BinarySearchTree as BST, Node as nd


class BinarySearchTreeTest(unittest.TestCase):
    """Test binary search tree components and objects"""

    def Node(self):
        """test node class"""
        node_value = nd(5100)
        node_expected_value = 5100
        self.assertEqual(node_value, node_expected_value)  # expecting true

        node_value = nd(5100)
        node_expected_value = 510
        self.assertNotEqual(node_value, node_expected_value)  # expecting false
    
    def BST_test(self):
        """test BST class including all of its inbuilt methods"""
        pass
