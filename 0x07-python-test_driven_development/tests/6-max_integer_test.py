#!/usr/bin/python3
"""
The Unittest for the module  max_integer([#,#,#])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Several tests for the function max_integer
    """

    def test_success(self):
        """tests successful cases of max_integer"""
        self.assertEqual(max_integer([10, 9, 8, 7, 6]), 10)
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([1, 1, 1]), 1)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 2, 20, 3, 3, 10, 10]), 20)
        self.assertEqual(max_integer([-1, -2, -3, -4, 0]), 0)
        self.assertEqual(max_integer([]), None)

    def test_error(self):
        """tests errors from incorrect type"""
        self.assertRaises(Exception, max_integer, ["Hello", 3.14, 25])

    def test_none(self):
        """tests errors if argument is none"""
        self.assertIsNone(max_integer())
