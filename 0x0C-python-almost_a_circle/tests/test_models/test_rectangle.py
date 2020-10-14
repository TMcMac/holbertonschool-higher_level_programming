#!/usr/bin/python3
"""unittest for Rectangle class"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Class for setting up unit tests for the class Rectangle
    """
    @classmethod
    def setUpRec(cls):
        pass

    @classmethod
    def tearDownRec(cls):
        pass

    def setUp(self):
        """
        Description:
             This sets up several recatngles for testing
        """
        self.r1 = Rectangle(5, 5)
        self.r2 = Rectangle(10, 10)
        self.r3 = Rectangle(5, 5, 0, 0, 4)
        self.r4 = Rectangle(20, 20, 2, 2, 5)
        self.r5 = Rectangle(3, 3, 1, 1, 6)
        self.r6 = Rectangle(9, 3, 0, 5)
        self.r7 = Rectangle(10, 2, 3, 3, 4)

    def tearDown(self):
        """
        Description:
            This will clean up / delete our test rectangles
        """
        del self.r1
        del self.r2
        del self.r3
        del self.r4
        del self.r5
        del self.r6
        del self.r7

    def test_aaaarectangle(self):
        """
        Testing passing case valid basic input to rectangle
        """
        self.assertEqual(self.r1.id, 23)
        self.assertEqual(self.r1.width, 5)
        self.assertEqual(self.r1.height, 5)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)

        self.assertEqual(self.r2.id, 24)
        self.assertEqual(self.r2.width, 10)
        self.assertEqual(self.r2.height, 10)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r2.y, 0)

        self.assertEqual(self.r3.id, 4)
        self.assertEqual(self.r3.width, 5)
        self.assertEqual(self.r3.height, 5)
        self.assertEqual(self.r3.x, 0)
        self.assertEqual(self.r3.y, 0)

        self.assertEqual(self.r4.id, 5)
        self.assertEqual(self.r4.width, 20)
        self.assertEqual(self.r4.height, 20)
        self.assertEqual(self.r4.x, 2)
        self.assertEqual(self.r4.y, 2)

        self.assertEqual(self.r5.id, 6)
        self.assertEqual(self.r5.width, 3)
        self.assertEqual(self.r5.height, 3)
        self.assertEqual(self.r5.x, 1)
        self.assertEqual(self.r5.y, 1)

        self.assertEqual(self.r6.id, 25)
        self.assertEqual(self.r6.width, 9)
        self.assertEqual(self.r6.height, 3)
        self.assertEqual(self.r6.x, 0)
        self.assertEqual(self.r6.y, 5)

        self.assertEqual(self.r7.id, 4)
        self.assertEqual(self.r7.width, 10)
        self.assertEqual(self.r7.height, 2)
        self.assertEqual(self.r7.x, 3)
        self.assertEqual(self.r7.y, 3)

    def test_rectangle_dimention_fail(self):
        """
        Failure conditions for dimentions
        """
        self.assertRaises(ValueError, Rectangle, width=10, height=0)
        self.assertRaises(ValueError, Rectangle, width=0, height=10)

    def test_rectangle_bad_offset(self):
        """
        This should raise an error for negative x or y values
        """
        self.assertRaises(Exception, Rectangle, width=10, height=10, x=-2, y=0)
        self.assertRaises(Exception, Rectangle, width=10, height=10, x=0, y=-2)

    def test_rectangle_bad_input(self):
        """
        This is to test the value error for rectangle
        """
        self.assertRaises(TypeError, Rectangle, "Hello", 10)
        self.assertRaises(TypeError, Rectangle, 10, "World")
        self.assertRaises(TypeError, Rectangle, 3.14, 5.2)
        self.assertRaises(TypeError, Rectangle, 'c', 'd')
        self.assertRaises(TypeError, Rectangle, [1, 2, 3], 10)
        self.assertRaises(TypeError, Rectangle, (2, 4), 10)

    def test_area(self):
        """
        This will test the area calculation on our test rectangle
        """
        self.assertEqual(Rectangle.area(self.r1), 25)
        self.assertEqual(Rectangle.area(self.r2), 100)
        self.assertEqual(Rectangle.area(self.r3), 25)
        self.assertEqual(Rectangle.area(self.r4), 400)
        self.assertEqual(Rectangle.area(self.r5), 9)
        self.assertEqual(Rectangle.area(self.r6), 27)
        self.assertEqual(Rectangle.area(self.r7), 20)

    def test_str(self):
        """
        This will test the sting output for a few of our rectangles
        """
        self.assertEqual(self.r1.__str__(), "[Rectangle] (60) 0/0 - 5/5")
        self.assertEqual(self.r2.__str__(), "[Rectangle] (61) 0/0 - 10/10")
        self.assertEqual(self.r3.__str__(), "[Rectangle] (4) 0/0 - 5/5")
        self.assertEqual(self.r4.__str__(), "[Rectangle] (5) 2/2 - 20/20")
        self.assertEqual(self.r5.__str__(), "[Rectangle] (6) 1/1 - 3/3")
        self.assertEqual(self.r6.__str__(), "[Rectangle] (62) 0/5 - 9/3")
        self.assertEqual(self.r7.__str__(), "[Rectangle] (4) 3/3 - 10/2")

    def test_update_args(self):
        """
        This will test the rectangle update method
        """
        self.assertEqual(self.r1.__str__(), "[Rectangle] (63) 0/0 - 5/5")
        self.r1.update(100)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (100) 0/0 - 5/5")
        self.r1.update(100, 7)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (100) 0/0 - 7/5")
        self.r1.update(100, 7, 9)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (100) 0/0 - 7/9")
        self.r1.update(100, 7, 9, 11, 11)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (100) 11/11 - 7/9")

    def test_update_kwargs(self):
        """
        This will test the rectangle update method
        """
        self.assertEqual(self.r1.__str__(), "[Rectangle] (66) 0/0 - 5/5")
        self.r1.update(id=100)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (100) 0/0 - 5/5")
        self.r1.update(id=100, width=7)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (100) 0/0 - 7/5")
        self.r1.update(id=100, width=7, height=9)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (100) 0/0 - 7/9")
        self.r1.update(id=100, width=7, height=9, y=11, x=11)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (100) 11/11 - 7/9")

    def test_w_to_dict(self):
        """
        This will test the dictionary method
        """
        self.assertEqual(self.r1.__str__(), "[Rectangle] (69) 0/0 - 5/5")
        self.r1.update(100, 10, 10, 1, 1)
        correct = {'x': 1, 'y': 1, 'id': 100, 'height': 10, 'width': 10}
        new_dict = self.r1.to_dictionary()
        self.assertIs(type(new_dict), dict)
        self.assertEqual(new_dict, correct)

    def test_class_docstring(self):
        """
        Description:
            Test to make sure class has a docstring
        """
        r1 = len(Rectangle.__doc__)
        self.assertTrue(r1 > 0, True)

    def test_init_for_docstring(self):
        """
        Description:
            Test to make sure init module has a docstring
        """
        r2 = len(Rectangle.__init__.__doc__)
        self.assertTrue(r2 > 0, True)

    def test_modules_docstring(self):
        """
        Description:
            Make sure modules have docstrings
        """
        r3 = len(__import__('models.rectangle').__doc__)
        self.assertTrue(r3 > 0, True)
