#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_positiveList(self):
        self.assertEqual(max_integer([9, 3, 15]), 15)

    def test_negativeList(self):
        self.assertEqual(max_integer([-9, -3, -15]), -3)

    def test_mixedList(self):
        self.assertEqual(max_integer([9, 3, -15]), 9)

    def test_emptyList(self):
        self.assertIsNone(max_integer([]))

if __name__ == "__main__":
    unittest.main()