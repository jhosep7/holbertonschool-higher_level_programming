#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
import pep8
from models.rectangle import Rectangle


class Testrectangle(unittest.TestCase):

    def test_pep8_conformance_rectangle(self):
        """Test that we conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0, "\
Found code style errors (and warnings).")

    def test_subclass(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def is_string(self):
        with self.assertRaises(TypeError):
            R1 = Rectangle(1.01, 3)
        with self.assertRaises(TypeError):
            R1 = Rectangle(1.01, 3)

    def test_type_param(self):
        """Task 3 """
        """ WIDTH TESTING """
        with self.assertRaises(TypeError):
            R1 = Rectangle(1.01, 3)
            raise TypeError()

        with self.assertRaises(ValueError):
            R2 = Rectangle(-234234242, 45)
            raise ValueError()

        with self.assertRaises(TypeError):
            R3 = Rectangle("", 4)
            raise TypeError()

        with self.assertRaises(TypeError):
            R4 = Rectangle(True, 4)
            raise TypeError()

        """ HEIGHT TESTING """
        with self.assertRaises(TypeError):
            H1 = Rectangle(5, 1.76)
            raise TypeError()

        with self.assertRaises(TypeError):
            H2 = Rectangle(5, "Hello")
            raise TypeError()

        with self.assertRaises(TypeError):
            H3 = Rectangle(5, False)
            raise TypeError()

        with self.assertRaises(ValueError):
            H1 = Rectangle(5, -4798576398576)
            raise ValueError()

        """ X TESTING """
        with self.assertRaises(TypeError):
            H1 = Rectangle(5, 1, 1.50)
            raise TypeError()

        with self.assertRaises(TypeError):
            H2 = Rectangle(5, 6, "test")
            raise TypeError()

        with self.assertRaises(TypeError):
            H3 = Rectangle(5, 7, False)
            raise TypeError()

        with self.assertRaises(ValueError):
            H1 = Rectangle(5, 7, -4798576398576)
            raise ValueError()

        """ Y TESTING """
        with self.assertRaises(TypeError):
            H1 = Rectangle(5, 1, 1, 1.53)
            raise TypeError()

        with self.assertRaises(TypeError):
            H2 = Rectangle(5, 6, 5, "test")
            raise TypeError()

        with self.assertRaises(TypeError):
            H3 = Rectangle(5, 7, 7, False)
            raise TypeError()

        with self.assertRaises(ValueError):
            H1 = Rectangle(5, 9, 5, -4798576398576)
            raise ValueError()

    def test_0_id(self):
        """
        Tests for id
        """
        Base._Base__nb_objects = 0
        R1 = Rectangle(10, 11)
        R2 = Rectangle(11, 12, 13)
        R3 = Rectangle(12, 13, 14, 15)
        R6 = Rectangle(13, 14, 15, 16, 5)
        R4 = Rectangle(2, 4, 5, 6, 7)
        R5 = Rectangle(3, 45, 4, 2, id="10")
        self.assertEqual(R1.id, 1)
        self.assertEqual(R2.id, 2)
        self.assertEqual(R3.id, 3)
        self.assertEqual(R6.id, 5)
        self.assertEqual(R4.id, 7)
        self.assertEqual(R5.id, "10")

    def test_1_arg(self):
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            Rectangle(10)
            Rectangle()
            Rectangle(x=10, y=20)

    def test_2_TypeError(self):
        Base._Base__nb_objects = 0
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Hello", 2)
            Rectangle(True, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "Hello")
            Rectangle(True, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, "Hello")
            Rectangle(True, 2, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 5, "Hello")
            Rectangle(True, 2, 4, 5)

    def test_2_TypeError(self):
        Base._Base__nb_objects = 0
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Hello", 2)
            Rectangle(True, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "Hello")
            Rectangle(True, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, "Hello")
            Rectangle(True, 2, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 5, "Hello")
            Rectangle(True, 2, 4, 5)

    def test_3_ValueError(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-3, 2)
            Rectangle(0, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, -2)
            Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(3, 2, -2)
            Rectangle(1, 2, 0)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 2, 2, -5)
            Rectangle(1, 2, 3, 0)

    def test_area(self):
        with self.assertRaises(TypeError):
            R = Rectangle()
            self.R.area(1)

if __name__ == "_main_":
    unittest.main()
