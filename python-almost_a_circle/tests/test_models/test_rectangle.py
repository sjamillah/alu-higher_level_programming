#!/usr/bin/python3
""" Module for test Rectangle class """
import unittest
import os
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleMethods(unittest.TestCase):
    """ Suite to test Rectangle class """

    def setUp(self):
        """ Method called for each test """
        Base._Base__nb_objects = 0

@classmethod
    def tearDown(cls):
        try:
            os.remove('Rectangle.json')
        except IOError:
            pass

    def test_right_argument(self):
        rect_1 = Rectangle(4, 2)
        rect_2 = Rectangle(2, 3, 8)
        rect_3 = Rectangle(2, 3, 8, 4)
        rect_4 = Rectangle(2, 3, 7, 3, 5)
        self.assertEqual(rect_1.x, 0)
        self.assertEqual(rect_1.y, 0)
        self.assertEqual(rect_1.width, 4)
        self.assertEqual(rect_1.height, 2)
        self.assertEqual(rect_2.x, 8)
        self.assertEqual(rect_1.y, 0)
        self.assertEqual(rect_3.x, 8)
        self.assertEqual(rect_3.y, 4)
        self.assertEqual(rect_4.id, 5)

    def test_no_position_argument_type(self):
        with self.assertRaises(TypeError) as error:
            Rectangle()
        message = "__init__() missing 2 required positional arguments: 'width' and 'height'"
        self.assertEqual(str(error.exception), message)
        with self.assertRaises(TypeError) as error:
            Rectangle(3)
        message = "__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(str(error.exception), message)
        with self.assertRaises(TypeError) as error:
            Rectangle(4, 4, 5, 6, 7, 8)
        message = "__init__() takes from 3 to 6 positional arguments but 7 were given"
        self.assertEqual(str(error.exception), message)

    def test_invalid_width(self):
        with self.assertRaises(TypeError) as error:
            Rectangle("3", 2)
        message = "width must be an integer"
        self.assertEqual(str(error.exception), message)
        with self.assertRaises(ValueError) as error:
            Rectangle(-4, 4)
        message = "width must be > 0"
        self.assertEqual(str(error.exception), message)
        with self.assertRaises(ValueError) as error:
            Rectangle(0, 4)
        message = "width must be > 0"
        self.assertEqual(str(error.exception), message)

    def test_invalid_height(self):
        with self.assertRaises(TypeError) as error:
            Rectangle(3, "2")
        message = "height must be an integer"
        self.assertEqual(str(error.exception), message)
        with self.assertRaises(ValueError) as error:
            Rectangle(4, -4)
        message = "height must be > 0"
        self.assertEqual(str(error.exception), message)
        with self.assertRaises(ValueError) as error:
            Rectangle(4, 0)
        message = "height must be > 0"
        self.assertEqual(str(error.exception), message)

    def test_invalid_x(self):
        with self.assertRaises(ValueError) as error:
            Rectangle(4, 4, -3)
        message = "x must be >= 0"
        self.assertEqual(str(error.exception), message)
        with self.assertRaises(TypeError) as error:
            Rectangle(4, 4, "4")
        message = "x must be an integer"
        self.assertEqual(str(error.exception), message)

    def test_invalid_y(self):
        with self.assertRaises(ValueError) as error:
            Rectangle(4, 4, 5, -6)
        message = "y must be >= 0"
        self.assertEqual(str(error.exception), message)
        with self.assertRaises(TypeError) as error:
            Rectangle(4, 4, 5, 'er')
        message = "y must be an integer"
        self.assertEqual(str(error.exception), message)

    def test_area(self):
        rect_1 = Rectangle(2, 2)
        self.assertEqual(rect_1.area(), 4)

    def test_str(self):
        shape = Rectangle(2, 2)
        shape2 = Rectangle(2, 5, 1, 3)
        self.assertEqual(str(shape), "[Rectangle] (1) 0/0 - 2/2")
        self.assertEqual(str(shape2), "[Rectangle] (2) 1/3 - 2/5")

    def test_display(self):
        shape = Rectangle(4, 2)
        shape1 = Rectangle(4, 2, 3)
        shape2 = Rectangle(4, 2, 3, 2)
        with patch('sys.stdout', n=StringIO()) as f:
            shape.display()
            self.assertEqual(f.getvalue(), "####\n####\n")

        with patch('sys.stdout', n=StringIO()) as f:
            shape1.display()
            self.assertEqual(f.getvalue(), "   ####\n   ####\n")

        with patch('sys.stdout', n=StringIO()) as f:
            shape2.display()
            self.assertEqual(f.getvalue(), "\n\n   ####\n   ####\n")

    def test_to_dictionary(self):
        shape = Rectangle(4, 2)
        self.assertEqual(shape.to_dictionary(), {"id": 1, 'width': 4, 'height': 2, 'x': 0, 'y': 0})

    def test_update(self):
        Base._Base__nb_objects = 0
        u1 = Rectangle(4, 2)

        u1.update()
        self.assertEqual(u1.id, 1)

        u1.update(89)
        self.assertEqual(u1.id, 89)

        u1.update(89, 1)
        self.assertEqual(u1.width, 1)
        self.assertEqual(u1.id, 89)

        u1.update(89, 1, 2)
        self.assertEqual(u1.height, 2)
        self.assertEqual(u1.width, 1)
        self.assertEqual(u1.id, 89)

        u1.update(89, 1, 2, 3)
        self.assertEqual(u1.height, 2)
        self.assertEqual(u1.width, 1)
        self.assertEqual(u1.id, 89)
        self.assertEqual(u1.x, 3)

        u1.update(89, 1, 2, 3, 4)
        self.assertEqual(u1.height, 2)
        self.assertEqual(u1.width, 1)
        self.assertEqual(u1.id, 89)
        self.assertEqual(u1.x, 3)
        self.assertEqual(u1.y, 4)

        u1.update(**{'id': 89})
        self.assertEqual(u1.id, 89)

        u1.update(**{'id': 89, 'width': 1})
        self.assertEqual(u1.id, 89)
        self.assertEqual(u1.width, 1)

        u1.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(u1.id, 89)
        self.assertEqual(u1.width, 1)
        self.assertEqual(u1.height, 2)

        u1.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(u1.id, 89)
        self.assertEqual(u1.width, 1)
        self.assertEqual(u1.height, 2)
        self.assertEqual(u1.x, 3)

        u1.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(u1.id, 89)
        self.assertEqual(u1.width, 1)
        self.assertEqual(u1.height, 2)
        self.assertEqual(u1.x, 3)
        self.assertEqual(u1.y, 4)

    def test_rectangle_create(self):
        shape = Rectangle.create(**{'id': 89})
        self.assertEqual(shape.id, 89)

        shape = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(shape.id, 89)
        self.assertEqual(shape.width, 1)

        shape = Rectangle(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(shape.id, 89)
        self.assertEqual(shape.width, 1)
        self.assertEqual(shape.height, 2)

        shape = Rectangle(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(shape.id, 89)
        self.assertEqual(shape.width, 1)
        self.assertEqual(shape.height, 2)
        self.assertEqual(shape.x, 3)

        shape = Rectangle(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(shape.id, 89)
        self.assertEqual(shape.width, 1)
        self.assertEqual(shape.height, 2)
        self.assertEqual(shape.x, 3)
        self.assertEqual(shape.y, 4)

    def test_save_to_file(self):
        Rectangle.save_to_file(None)
        with open('Rectangle.json', 'r', encoding="utf-8") as f:
            text = f.read()
        self.assertEqual(text, '[]')
        shape = Rectangle(2, 2)
        Rectangle.save_to_file([shape])
        with open('Rectangle.json', 'r', encoding="utf-8") as f:
            text = f.read()
            self.assertEqual(Base.from_json_string(text), [{'id': 1, 'width': 2, 'height': 2, 'x': 0, 'y': 0}])

    def test_save_to_file_empy_list(self):
        Rectangle.save_to_file([])
        with open('Rectangle.json', 'r', encoding="utf-8") as f:
            text = f.read()
        self.assertEqual(text, '[]')

    def test_load_from_file_no_file(self):
        shapes = Rectangle.load_from_file()
        self.assertEqual(shapes, [])

    def test_load_from_file_file_exists(self):
        shape = Rectangle(2, 2)
        Rectangle.save_to_file([shape])
        returnedShape = Rectangle.load_from_file()
        self.assertEqual(returnedShape[0].to_dictionary(), shape.to_dictionary())
