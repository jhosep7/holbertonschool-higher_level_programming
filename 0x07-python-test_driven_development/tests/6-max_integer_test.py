#!/usr/bin/python3
"""Unit Test to Check Max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_noArgc(self):
        self.assertIsNone(max_integer())

    def test_PosInt(self):
        self.assertEqual(max_integer([1, 2, 5, 7]), 7)
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_NegInt(self):
        self.assertEqual(max_integer([-1, -2, -5, -7]), -1)
        self.assertEqual(max_integer([7, -7, -7, 7]), 7)

    def test_OneElement(self):
        self.assertEqual(max_integer([33]), 33)

    def test_MixedVals(self):
        with self.assertRaises(TypeError):
            max_integer(["Yup", 11, "12", -3.5, 7])
        with self.assertRaises(TypeError):
            max_integer(["Yup", 11, "12", -3.5, [7]])

    def test_EmptyList(self):
        self.assertIsNone(max_integer([]), None)

    def test_String(self):
        self.assertEqual(max_integer(["abc", "xyz"]), "xyz")
        self.assertEqual(max_integer("1, 2, 3"), "3")

if __name__ == "__main__":
    unittest.main()
