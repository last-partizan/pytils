# -*- coding: utf-8 -*-
# pytils - russian-specific string utils
# Copyright (C) 2006-2009  Yury Yurevich
#
# http://pyobject.ru/projects/pytils/
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
from __future__ import print_function, absolute_import, division, unicode_literals

import unittest

from pytils import templatetags as tt

class TemplateTagsCommonsTestCase(unittest.TestCase):
    
    def testInitDefaults(self):
        """
        Unit-tests for pytils.templatetags.init_defaults
        """
        self.assertEquals(tt.init_defaults(debug=False, show_value=False), ('', ''))
        self.assertEquals(tt.init_defaults(debug=False, show_value=True), ('%(value)s', '%(value)s'))
        self.assertEquals(tt.init_defaults(debug=True, show_value=False), ('unknown: %(error)s', 'unknown: %(error)s'))
        self.assertEquals(tt.init_defaults(debug=True, show_value=True), ('unknown: %(error)s', 'unknown: %(error)s'))
    
    def testPseudoUnicode(self):
        """
        Unit-tests for pytils.templatetags.pseudo_unicode
        """
        str_value = 'тест'.encode('utf-8')
        self.assertEquals(tt.pseudo_unicode(str_value, 'utf-8'), 'тест')
        self.assertEquals(tt.pseudo_unicode(str_value, 'utf-8'), 'тест')
        self.assertEquals(tt.pseudo_unicode(str_value, 'ascii'), '')
        self.assertEquals(tt.pseudo_unicode(str_value, 'ascii', 'опа'), 'опа')
        self.assertRaises(UnicodeDecodeError, tt.pseudo_unicode, str_value, 'ascii', None)


if __name__ == '__main__':
    unittest.main()
