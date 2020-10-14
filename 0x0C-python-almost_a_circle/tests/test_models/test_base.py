#!/usr/bin/python3
"""unittest for Base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Testing Base class
    """

   @classmethod
    def setUpBase(cls):
        pass

    @classmethod
    def tearDownBase(cls):
        pass

    def setUp(self):
        """
        Description:
            Creates several base objects for testing
        """
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b0 = Base(0)
        self.b4 = Base(4)
        self.b5 = Base(5)
        self.b6 = Base()
        self.b9 = Base(9)
        self.b7 = Base()
        self.bneg = Base(-5)
        self.bchar = Base('q')
        self.bpie = Base(3.14)
        self.blist = Base([1, 2, 3])
        self.btuple = Base((2, 4))

    def tearDown(self):
        """
        Description:
            Deletes or removes out test cases
        """
        del self.b1
        del self.b2
        del self.b3
        del self.b0
        del self.b4
        del self.b5
        del self.b6
        del self.b9
        del self.b7
        del self.bneg
        del self.bchar
        del self.bpie
        del self.blist
        del self.btuple

    def test_aabase_id(self):
        """
        Description:
            Test creating an instance without
            any input to make sure id works
        """
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b0.id, 0)
        self.assertEqual(self.b4.id, 4)
        self.assertEqual(self.b5.id, 5)
        self.assertEqual(self.b6.id, 4)
        self.assertEqual(self.b9.id, 9)
        self.assertEqual(self.b7.id, 5)
        self.assertEqual(self.bneg.id, -5)
        self.assertEqual(self.bchar.id, 'q')
        self.assertEqual(self.bpie.id, 3.14)
        self.assertEqual(self.blist.id, [1, 2, 3])
        self.assertEqual(self.btuple.id, (2, 4))

#    def test_base_id_collision(self):
#        """
#        Description:
#            Test to see if id assignments collides
#        """
#        self.assertTrue(b6.isinstance(Base))
#        self.assertTrue(b7.isinstance(Base))
#        self.assertFalse(b4.isinstance(None))
#        self.assertFalse(b5.isinstance(None))

    def test_class_docstring(self):
        """
        Description:
            Test to make sure class has a docstring
        """
        b1 = len(Base().__doc__)
        self.assertTrue(b1 > 0, True)

    def test_init_for_docstring(self):
        """
        Description:
            Test to make sure init module has a docstring
        """
        b2 = len(Base().__init__.__doc__)
        self.assertTrue(b2 > 0, True)

    def test_module_for_docstring(self):
        """
        Description:
            Tests each module for a docstring
        """
        b3 = len(__import__('models.base').__doc__)
        self.assertTrue(b3 > 0, True)

    def test_pep8(self):
        """
        tests code for pep8 style guidelines
        """
        import pep8
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py',
                                        'models/rectangle.py',
                                        'models/square.py'])
        self.assertEqual(result.total_errors, 0,
                            "Found code style errors (and warnings).")
