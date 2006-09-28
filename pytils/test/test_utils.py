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


if __name__ == '__main__':
    unittest.main()
