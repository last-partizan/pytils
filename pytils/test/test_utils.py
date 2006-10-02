# -*- coding: utf-8 -*-
# License: GNU GPL2
# Author: Pythy <the.pythy@gmail.com>
"""
Unit-tests for pytils.utils
"""

__id__ = __revision__ = "$Id$"
__url__ = "$URL$"

import unittest
import pytils 

class UnicodeTestCase(unittest.TestCase):
    """
    Test case for unicode-utils 
    """

    def ckProvideUnicode(self, stext, encoding, utext):
        """
        Check pytils.provide_unicode
        """
        self.assertEquals(
            pytils.utils.provide_unicode(stext, encoding),
            utext
            )

    def ckProvideStr(self, utext, encoding, stext):
        """
        Check pytils.provide_str
        """
        self.assertEquals(
            pytils.utils.provide_str(utext, encoding),
            stext
            )

    def testProvideUnicode(self):
        """
        Unit-tests for pytils.utils.provide_unicode
        """
        self.ckProvideUnicode("тест №1", "utf-8", u"тест №1")

    def testProvideStr(self):
        """
        Unit-tests for pytils.utils.provide_str
        """
        self.ckProvideStr(u"тест №1", "utf-8", "тест №1")
        self.ckProvideStr(u"тест №1", "koi8-r", "unknown")

    def testProvideStrNonDefault(self):
        """
        Unit-tests for pytils.utils.provide_str with 'default' parameter
        """
        self.assertEquals(
            pytils.utils.provide_str(u"тест №1", "koi8-r", default="hz"),
            "hz"
            )

class ChecksTestCase(unittest.TestCase):
    """
    Test case for check_* utils
    """

    def testGetValueByName(self):
        """
        Unit-test for pytils.utils.get_value_by_name
        """
        var1 = '25'
        var2 = 25
        self.assertEquals('25', pytils.utils.get_value_by_name('var1', depth=1))
        self.assertEquals(25, pytils.utils.get_value_by_name('var2', depth=1))
        self.assertRaises(RuntimeError, pytils.utils.get_value_by_name, 'var3')
        

    def testCheckType(self):
        """
        Unit-test for pytils.utils.check_type
        """
        var = '25'
        # нельзя assertRaises, потому что глубина стека вызовов тогда не 2,
        # а гораздо больше
        try:
            pytils.utils.check_type('var', int)
        except TypeError, err:
            self.assertEquals("var must be <type 'int'>, not <type 'str'>",
                              str(err))
        try:
            pytils.utils.check_type('var', (int, float))
        except TypeError, err:
            self.assertEquals("var must be (<type 'int'>, <type 'float'>), " + \
                              "not <type 'str'>",
                              str(err))
        self.assertEquals(None, pytils.utils.check_type('var', str))
        self.assertEquals(None, pytils.utils.check_type('var',
                                                        (str, basestring)))

    def testCheckLength(self):
        """
        Unit-test for pytils.utils.check_length
        """
        var = 'test'
        self.assertEquals(None, pytils.utils.check_length('var', 4))
        try:
            pytils.utils.check_length('var', 5)
        except ValueError, err:
            self.assertEquals("var's length must be 5, but it 4",
                              str(err))

    def testCheckPositive(self):
        """
        Unit-test for pytils.utils.check_positive
        """
        var1 = 1
        var2 = 1.25
        var3 = -2
        var4 = -2.12

        self.assertEquals(None, pytils.utils.check_positive('var1'))
        self.assertEquals(None, pytils.utils.check_positive('var2'))

        try:
            pytils.utils.check_positive('var3')
        except ValueError, err:
            self.assertEquals("var3 must be positive or zero, not -2",
                              str(err))
        try:
            pytils.utils.check_positive('var4')
        except ValueError, err:
            self.assertEquals("var4 must be positive or zero, not -2.12",
                              str(err))


if __name__ == '__main__':
    unittest.main()
