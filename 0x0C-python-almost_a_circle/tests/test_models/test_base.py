#!/usr/bin/python3
"""unittest for Base class"""


import unittest
import pep8

from models.base import Base


class Test_a_Base(unittest.TestCase):
    """testing Base class"""

        def test_pep8(self):
        """tests code for pep8 style guidelines"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py',
                                        'models/rectangle.py',
                                        'models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
