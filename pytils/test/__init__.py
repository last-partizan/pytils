# -*- coding: utf-8 -*-
# License: GNU GPL2
# Author: Pythy <the.pythy@gmail.com>
"""
Unit tests for pytils
"""

__id__ = __revision__ = "$Id$"
__url__ = "$URL$"
__all__ = ["test_numeral", "test_dt", "test_translit"]

import unittest

def get_suite():
    """Return TestSuite for all unit-test of PyTils"""
    suite = unittest.TestSuite()
    for module_name in __all__:
        imported_module = __import__("pytils.test."+module_name,
                                       globals(),
                                       locals(),
                                       ["pytils.test"])
        loader = unittest.defaultTestLoader
        suite.addTest(loader.loadTestsFromModule(imported_module))

    return suite

def run(verbosity=1):
    """Run all unit-test of PyTils"""
    suite = get_suite()
    unittest.TextTestRunner(verbosity=verbosity).run(suite)

if __name__ == '__main__':
    run(2)
