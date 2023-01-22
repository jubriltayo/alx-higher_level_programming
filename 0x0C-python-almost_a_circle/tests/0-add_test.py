#!/usr/bin/python3
"""Unittest to test the function that sums two integers"""

import unittest
add = __import__('0-add').add


class TestAdd(unittest.TestCase):
    """Test cases"""

    def test_int(self):
        """test for integers"""
        self.assertEqual(add(5, 4), 9)

    def test_float(self):
        """test for float"""
        self.assertEqual(add(4.5, 6), 10)

    def test_neg_int(self):
        """test for negative integers"""
        self.assertEqual(add(-4, 7), 3)

    def test_zero(self):
        """test for zero"""
        self.assertEqual(add(5, 0), 5)
