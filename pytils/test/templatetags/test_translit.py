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
Unit tests for pytils' translit templatetags for Django web framework
"""

from pytils.test.templatetags import helpers

class TranslitDefaultTestCase(helpers.TemplateTagTestCase):
    
    def testLoad(self):
        self.check_template_tag('load_tag', u'{% load pytils_translit %}', {}, u'')
    
    def testTranslifyFilter(self):
        self.check_template_tag('translify_filter', 
            u'{% load pytils_translit %}{{ val|translify }}', 
            {'val': 'проверка'}, 
            u'proverka')
    
    def testDetranslifyFilter(self):
        self.check_template_tag('detranslify_filter', 
            u'{% load pytils_translit %}{{ val|detranslify }}', 
            {'val': 'proverka'}, 
            u'проверка')

    def testSlugifyFilter(self):
        self.check_template_tag('slugify_filter', 
            u'{% load pytils_translit %}{{ val|slugify }}', 
            {'val': 'Проверка связи'}, 
            u'proverka-svyazi')
    
    # без отладки, если ошибка -- по умолчанию пустая строка
    def testDetranslifyError(self):
        # в юникод-режиме это не ошибка
        from pytils.templatetags import unicode_aware
        if not unicode_aware:
            self.check_template_tag('detranslify_error', 
                u'{% load pytils_translit %}{{ val|detranslify }}', 
                {'val': 'Проверка связи'}, 
                u'')


if __name__ == '__main__':
    import unittest
    unittest.main()
