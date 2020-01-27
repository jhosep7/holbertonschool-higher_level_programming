#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_id(self):
        S1 = Square(1)
        S2 = Square(1, 2)
        S3 = Square(1, 2, 3)
        S4 = Square(1, 2, 3, 4)
        self.assertEqual(S2.x, 2)
        self.assertEqual(S3.y, 3)
        self.assertEqual(S4.id, 4)

    def test_ValueError(self):
        Base._Base__nb_objects = 0
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-2)
            Square(0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(10, -3)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(10, 14, -5)

    def test_2_TypeError(self):
        Base._Base__nb_objects = 0
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("22")
            Square(True)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, "yup")
            Square(10, True)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 11, "hi")
            Square(10, 15, False)

    def test_3_str(self):

        Base._Base__nb_objects = 0
        S1 = Square(3)
        S2 = Square(3, 4)
        S3 = Square(3, 4, 5)
        self.assertEqual(S1.__str__(), "[Square] (1) 0/0 - 3")
        self.assertEqual(S2.__str__(), "[Square] (2) 4/0 - 3")
        self.assertEqual(S3.__str__(), "[Square] (3) 4/5 - 3")
