# Author: Francis Osei Annin
# Date: 14/04/23
# Description: A test stack data structure

import unittest
from ds.fundamentals.stack.stack import Stack


class TestStack(unittest.TestCase):
    """test stack data structure"""

    def test_is_empty(self):
        """test if stack is empty or not"""
        _stack = Stack()
        expected = False
        observed = _stack.is_empty()
        self.assertAlmostEqual(observed, expected)

    def test_peek_and_pop(self):
        """test stack peek method"""
        _stack = Stack()
        # add elements to add stack
        _stack.push(3)
        _stack.push(30)
        _stack.push(300)
        _stack.push(3000)

        # return first element on stack
        observed_peek_number = _stack.peek()
        expected_peek_number = 3000

        # return first number on stack but removes it
        observed_pop_number = _stack.pop()
        expected_pop_number = 3000

        self.assertAlmostEqual(observed_peek_number, expected_peek_number)
        self.assertAlmostEqual(observed_pop_number, expected_pop_number)


