#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests different scenarios"""

    def test_end(self):
        """Test for max if at the end"""
        sample = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(sample), 5)

    def test_beginning(self):
        """Test for max if at the beginning"""
        sample = [7, 2, 3, 4, 1]
        self.assertEqual(max_integer(sample), 7)

    def test_middle(self):
        """Test for max if at the middle"""
        sample = [5, 2, 9, 4, 1]
        self.assertEqual(max_integer(sample), 9)

    def test_negative(self):
        """Test for max if one negative value exists"""
        sample = [5, -2, 9, 4, 1]
        self.assertEqual(max_integer(sample), 9)

    def test_allnegative(self):
        """Test for max if all are negative values"""
        sample = [-5, -2, -9, -4, -1]
        self.assertEqual(max_integer(sample), -1)

    def test_one_element(self):
        """Test for max if only one element exist"""
        sample = [5]
        self.assertEqual(max_integer(sample), 5)

    def test_void(self):
        """Test for max if void"""
        sample = []
        self.assertEqual(max_integer(sample), None)
