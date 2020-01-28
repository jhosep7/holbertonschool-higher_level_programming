#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
import pep8
from models.rectangle import Rectangle

class TestBaseClassCreation(unittest.TestCase):
    def test_pep8_conformance_base(self):
    	pep8style = pep8.StyleGuide(quiet=True)
    	result = pep8style.check_files(['models/base.py'])
    	self.assertEqual(result.total_errors, 0,
                     	"Found code style errors (and warnings).")
    def test_id_positive(self):
        bo = Base(23)
        self.assertEqual(bo.id, 23)
        bo = Base(34)
        self.assertEqual(bo.id, 34)
    def test_id_negative(self):
        bo = Base(-4)
        self.assertEqual(bo.id, -4)
        bo = Base(-10)
        self.assertEqual(bo.id, -10)

    def test_id_string(self):
        bo = Base("st")
        self.assertEqual(bo.id, "st")
        bo = Base("st2")
        self.assertEqual(bo.id, "st2")
    def test_type(self):
        """ Test type and instance """
        b = Base()
        self.assertEqual(type(b), Base)
        self.assertTrue(isinstance(b, Base))

    def test_to_json_string(self):
        """ Test to_json_string functionality """
        d = {'id': 1, 'x': 2, 'y': 3, 'width': 4, 'height': 5}
        json_d = Base.to_json_string([d])
        self.assertTrue(isinstance(d, dict))
        self.assertTrue(isinstance(json_d, str))
        self.assertCountEqual(
            json_d, '{["id": 1, "x": 2, "y": 3, "width": 4, "height": 5]}')
        json_d_1 = Base.to_json_string(None)
        self.assertEqual(json_d_1, "[]")
        err = ("to_json_string() missing 1 required positional argument: " +
               "'list_dictionaries'")
        with self.assertRaises(TypeError) as e:
            Base.to_json_string()
        self.assertEqual(err, str(e.exception))
        err = "to_json_string() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            Base.to_json_string([{1, 2}], [{3, 4}])
        self.assertEqual(err, str(e.exception))
    def test_save_to_file(self):
        """Test class method save_to_file with normal types."""
        with self.assertRaises(AttributeError) as e:
            Base.save_to_file([Base(1), Base(2)])
        self.assertEqual(
             "'Base' object has no attribute 'to_dictionary'", str(
                e.exception))
   
    def test_create(self):
        """ Test create functionality """
        with self.assertRaises(TypeError) as e:
            err = Rectangle.create("str")
        self.assertEqual(
            "create() takes 1 positional argument but 2 were given", str(
                e.exception))

    def test_dictionary(self):
        """Comment"""
        re1 = Rectangle(10, 7, 2, 8, 70)
        dictionary = re1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(json_dictionary), str)

    def test_dictionary_empty(self):
        """Comment"""
        dictionary = []
        json_dictionary = Base.to_json_string(dictionary)
        self.assertEqual(json_dictionary, "[]")
        obj = None
        json_dictionary = Base.to_json_string(obj)
        self.assertEqual(json_dictionary, "[]")

    def test_13_file_square(self):
        S1 = Square(22)
        S2 = Square(44, 44, 55, 66)
        lS = [S1, S2]
        Square.save_to_file(lS)
        lS2 = Square.load_from_file()
        self.assertNotEqual(lS, lS2)
