#!/usr/bin/python3
"""File for testing class Square, which inherits from Rectangle"""
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquare(unittest.TestCase):
    """
    Class for setting up unit tests for the class Rectangle
    """
    @classmethod
    def setUpSqr(cls):
        pass

    @classmethod
    def tearDownSqr(cls):
        pass

    def setUp(self):
        """
        Description:
             This sets up several squares for testing
        """
        self.s1 = Square(5)
        self.s2 = Square(10)
        self.s3 = Square(5, 0, 0, 4)
        self.s4 = Square(20, 2, 2, 5)
        self.s5 = Square(3, 1, 1, 6)
        self.s6 = Square(9, 3, 0)
        self.s7 = Square(10, 3, 3, 5)

    def tearDown(self):
        """
        Description:
            This will clean up / delete our test squares
        """
        del self.s1
        del self.s2
        del self.s3
        del self.s4
        del self.s5
        del self.s6
        del self.s7

    def test_aaasquare_init(self):
        """
        Description:
            This will test the initial attributes of each square
        """
        self.assertIsNotNone(self.s1)
        self.assertEqual(self.s1.id, 72)
        self.assertEqual(self.s1.width, 5)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s1.y, 0)
        self.assertIs(type(self.s1), Square)
        self.assertIsInstance(self.s1, Rectangle)

        self.assertIsNotNone(self.s2)
        self.assertEqual(self.s2.id, 73)
        self.assertEqual(self.s2.width, 10)
        self.assertEqual(self.s2.x, 0)
        self.assertEqual(self.s2.y, 0)
        self.assertIs(type(self.s2), Square)
        self.assertIsInstance(self.s2, Rectangle)

        self.assertIsNotNone(self.s3)
        self.assertEqual(self.s3.id, 4)
        self.assertEqual(self.s3.width, 5)
        self.assertEqual(self.s3.x, 0)
        self.assertEqual(self.s3.y, 0)
        self.assertIs(type(self.s3), Square)
        self.assertIsInstance(self.s3, Rectangle)

        self.assertIsNotNone(self.s4)
        self.assertEqual(self.s4.id, 5)
        self.assertEqual(self.s4.width, 20)
        self.assertEqual(self.s4.x, 2)
        self.assertEqual(self.s4.y, 2)
        self.assertIs(type(self.s4), Square)
        self.assertIsInstance(self.s4, Rectangle)

        self.assertIsNotNone(self.s5)
        self.assertEqual(self.s5.id, 6)
        self.assertEqual(self.s5.width, 3)
        self.assertEqual(self.s5.x, 1)
        self.assertEqual(self.s5.y, 1)
        self.assertIs(type(self.s5), Square)
        self.assertIsInstance(self.s5, Rectangle)

        self.assertIsNotNone(self.s6)
        self.assertEqual(self.s6.id, 74)
        self.assertEqual(self.s6.width, 9)
        self.assertEqual(self.s6.x, 3)
        self.assertEqual(self.s6.y, 0)
        self.assertIs(type(self.s6), Square)
        self.assertIsInstance(self.s6, Rectangle)

        self.assertIsNotNone(self.s7)
        self.assertEqual(self.s7.id, 5)
        self.assertEqual(self.s7.width, 10)
        self.assertEqual(self.s7.x, 3)
        self.assertEqual(self.s7.y, 3)
        self.assertIs(type(self.s7), Square)
        self.assertIsInstance(self.s7, Rectangle)

    def test_area(self):
        """
        Description:
            Testing the square area module
        """
        self.assertEqual(Square.area(self.s1), 25)
        self.assertEqual(Square.area(self.s2), 100)
        self.assertEqual(Square.area(self.s3), 25)
        self.assertEqual(Square.area(self.s4), 400)
        self.assertEqual(Square.area(self.s5), 9)
        self.assertEqual(Square.area(self.s6), 81)
        self.assertEqual(Square.area(self.s7), 100)

    def test_bad_input(self):
        """
        This is to test the value error for rectangle
        """
        self.assertRaises(TypeError, Square, "Hello")
        self.assertRaises(TypeError, Square, 3.14)
        self.assertRaises(TypeError, Square, 'c')
        self.assertRaises(TypeError, Square, [1, 2, 3])
        self.assertRaises(TypeError, Square, (2, 4))

    def test_str(self):
        """
        This will test the sting output for a few of our Square
        """
        self.assertEqual(self.s1.__str__(), "[Square] (95) 0/0 - 5")
        self.assertEqual(self.s2.__str__(), "[Square] (96) 0/0 - 10")
        self.assertEqual(self.s3.__str__(), "[Square] (4) 0/0 - 5")
        self.assertEqual(self.s4.__str__(), "[Square] (5) 2/2 - 20")
        self.assertEqual(self.s5.__str__(), "[Square] (6) 1/1 - 3")
        self.assertEqual(self.s6.__str__(), "[Square] (97) 3/0 - 9")
        self.assertEqual(self.s7.__str__(), "[Square] (5) 3/3 - 10")

    def test_update_args(self):
        """
        This will test the Square update method
        """
        self.assertEqual(self.s1.__str__(), "[Square] (98) 0/0 - 5")
        self.s1.update(100)
        self.assertEqual(self.s1.__str__(), "[Square] (100) 0/0 - 5")
        self.s1.update(100, 7)
        self.assertEqual(self.s1.__str__(), "[Square] (100) 0/0 - 7")
        self.s1.update(100, 7, 11, 11)
        self.assertEqual(self.s1.__str__(), "[Square] (100) 11/11 - 7")

    def test_update_kwargs(self):
        """
        This will test the rectangle update method
        """
        self.assertEqual(self.s1.__str__(), "[Square] (101) 0/0 - 5")
        self.s1.update(id=100)
        self.assertEqual(self.s1.__str__(), "[Square] (100) 0/0 - 5")
        self.s1.update(id=100, size=7)
        self.assertEqual(self.s1.__str__(), "[Square] (100) 0/0 - 7")
        self.s1.update(id=100, size=7, y=11, x=12)
        self.assertEqual(self.s1.__str__(), "[Square] (100) 12/11 - 7")


    def test_class_docstring(self):
        """
        Description:
            Test to make sure class has a docstring
        """
        s1 = len(Square.__doc__)
        self.assertTrue(s1 > 0, True)

    def test_init_for_docstring(self):
        """
        Description:
            Test to make sure init module has a docstring
        """
        s2 = len(Square.__init__.__doc__)
        self.assertTrue(s2 > 0, True)

    def test_modules_docstring(self):
        """
        Description:
            Make sure modules have docstrings
        """
        s3 = len(__import__('models.square').__doc__)
        self.assertTrue(s3 > 0, True)
