"""
program: test_operations_practice.py
Author: Cassandra Wruck
Last Date Modified: June 7th, 2020

This is a test program to show the understanding of the operations.
"""

import unittest

class OperatorsTest(unittest.TestCase):

    #teacher example
    def test_equal(self):
        self.assertTrue(5 == 5)

    #all operations listed
    def test_equal_operator(self):
        a = 7
        b = -2
        self.assertFalse(a == b)

    def test_notequal_operator(self):
        a = 4
        b = 4
        self.assertFalse(a != b)

    def test_greaterthan_operator(self):
        a = 9
        b = 13
        self.assertFalse(a > b)

    def test_lessthan_operator(self):
        a = 10
        b = 2
        self.assertFalse(a < b)

    def test_greaterequalto_operator(self):
        a = 13
        b = 13
        self.assertTrue(a >= b)

    def test_lessequalto_operator(self):
        a = 2
        b = 3
        self.assertTrue(a <= b)


if __name__ == '__main__':
    unittest.main()
