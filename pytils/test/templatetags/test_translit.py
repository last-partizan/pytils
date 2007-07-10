# -*- coding: utf-8 -*-
# pytils - simple processing for russian strings
# Copyright (C) 2006-2007  Yury Yurevich
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

__id__ = __revision__ = "$Id$"
__url__ = "$URL$"

from pytils.test.templatetags import helpers

class TranslitDefaultTestCase(helpers.TemplateTagTestCase):
    
    def testLoad(self):
        self.check_template_tag('load_tag', '{% load pytils_translit %}', {}, '')
    
    def testTranslifyFilter(self):
        self.check_template_tag('translify_filter', 
            '{% load pytils_translit %}{{ val|translify }}', 
            {'val': 'проверка'}, 
            'proverka')
    
    def testDetranslifyFilter(self):
        self.check_template_tag('detranslify_filter', 
            '{% load pytils_translit %}{{ val|detranslify }}', 
            {'val': 'proverka'}, 
            'проверка')        

    def testSlugifyFilter(self):
        self.check_template_tag('slugify_filter', 
            '{% load pytils_translit %}{{ val|slugify }}', 
            {'val': 'Проверка связи'}, 
            'proverka-svyazi')
    
    # без отладки, если ошибка -- по умолчанию пустая строка
    def testDetranslifyError(self):
        self.check_template_tag('detranslify_error', 
            '{% load pytils_translit %}{{ val|detranslify }}', 
            {'val': 'Проверка связи'}, 
            '')


if __name__ == '__main__':
    import unittest
    unittest.main()
