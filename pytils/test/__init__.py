# -*- coding: utf-8 -*-
# License: GNU GPL2
# Author: Pythy <the.pythy@gmail.com>
"""
Unit tests for pytils
"""

__id__ = "$Id$"
__url__ = "$URL$"
__all__ = ["test_numeral", "test_dt", "test_translit"]

import unittest

def get_suite():
    suite = unittest.TestSuite()
    for module_name in __all__:
        imported_module = __import__("pytils.test."+module_name,
                                       globals(),
                                       locals(),
                                       ["pytils.test"])
        for e in dir(imported_module):
            element = getattr(imported_module, e)
            try:
                if issubclass(element, unittest.TestCase) or \
                   issubclass(element, unittest.TestSuite):
                    suite.addTest(unittest.makeSuite(element))
            except TypeError:
                # если element не класс
                pass

    return suite

def run(verbosity=1):
    suite = get_suite()
    unittest.TextTestRunner(verbosity=verbosity).run(suite)

if __name__ == '__main__':
    run(2)
