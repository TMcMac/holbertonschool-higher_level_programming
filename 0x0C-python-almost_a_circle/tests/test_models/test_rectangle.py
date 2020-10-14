#!/usr/bin/python3
"""unittest for Rectangle class"""


import unittest
import pep8

from models.rectangle import Rectangle


class Test_a_Rectangle(unittest.TestCase):
    """
    testing Rectangle class
    """
    def test_pep8(self):
    """
    tests code for pep8 style guidelines
    """
    pep8style = pep8.StyleGuide(quiet=True)
    result = pep8style.check_files(['models/base.py',
                                    'models/rectangle.py',
                                    'models/square.py'])
    self.assertEqual(result.total_errors, 0,
                        "Found code style errors (and warnings).")
