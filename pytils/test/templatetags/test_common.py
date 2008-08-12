# -*- coding: utf-8 -*-
# pytils - russian-specific string utils
# Copyright (C) 2006-2008  Yury Yurevich
#
# http://www.pyobject.ru/projects/pytils/
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, version 2
# of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
"""
Unit tests for pytils' templatetags common things
"""

import unittest

from pytils import templatetags as tt

class TemplateTagsCommonsTestCase(unittest.TestCase):
    
    def testInitDefaults(self):
        """
        Unit-tests for pytils.templatetags.init_defaults
        """
        self.assertEquals(tt.init_defaults(debug=False, show_value=False), ('', u''))
        self.assertEquals(tt.init_defaults(debug=False, show_value=True), ('%(value)s', u'%(value)s'))
        self.assertEquals(tt.init_defaults(debug=True, show_value=False), ('unknown: %(error)s', u'unknown: %(error)s'))
        self.assertEquals(tt.init_defaults(debug=True, show_value=True), ('unknown: %(error)s', u'unknown: %(error)s'))
    
    def testPseudoUnicode(self):
        """
        Unit-tests for pytils.templatetags.pseudo_unicode
        """
        self.assertEquals(tt.pseudo_unicode(u'тест', 'utf-8'), u'тест')
        self.assertEquals(tt.pseudo_unicode('тест', 'utf-8'), u'тест')
        self.assertEquals(tt.pseudo_unicode('тест', 'ascii'), u'')
        self.assertEquals(tt.pseudo_unicode('тест', 'ascii', u'опа'), u'опа')
        self.assertRaises(UnicodeDecodeError, tt.pseudo_unicode, 'тест', 'ascii', None)

    def testPseudoStr(self):
        """
        Unit-tests for pytils.templatetags.pseudo_str
        """
        # in django unicode-branch either str() must return unicode
        # this test depends on Django unicode awareness
        if tt.unicode_aware:
            self.assertEquals(tt.pseudo_str(u'тест', 'utf-8'), u'тест')
            self.assertEquals(tt.pseudo_str(u'тест', 'utf-8'), u'тест')
            self.assertEquals(tt.pseudo_str('тест', 'utf-8'), '')
            self.assertEquals(tt.pseudo_str('тест', 'utf-8', u'опа'), u'опа')
            self.assertEquals(tt.pseudo_str(u'тест', 'ascii'), u'тест')
            self.assertEquals(tt.pseudo_str(u'тест', 'ascii', 'опа'), u'тест')
        else:
            self.assertEquals(tt.pseudo_str(u'тест', 'utf-8'), 'тест')
            self.assertEquals(tt.pseudo_str('тест', 'utf-8'), '')
            self.assertEquals(tt.pseudo_str(u'тест', 'ascii'), '')
            self.assertEquals(tt.pseudo_str(u'тест', 'ascii', 'опа'), 'опа')
            self.assertRaises(UnicodeEncodeError, tt.pseudo_str, u'тест', 'ascii', None)


if __name__ == '__main__':
    unittest.main()
