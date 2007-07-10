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
Unit tests for pytils' numeral templatetags for Django web framework
"""

__id__ = __revision__ = "$Id$"
__url__ = "$URL$"

from pytils.test.templatetags import helpers

class NumeralDefaultTestCase(helpers.TemplateTagTestCase):

    def testLoad(self):
        self.check_template_tag('load_tag', '{% load pytils_numeral %}', {}, '')
    
    def testChoosePluralFilter(self):
        self.check_template_tag('choose_plural', 
            '{% load pytils_numeral %}{{ val|choose_plural:"гвоздь,гвоздя,гвоздей" }}', 
            {'val': 10},
            'гвоздей')

    def testGetPluralFilter(self):
        self.check_template_tag('get_plural', 
            '{% load pytils_numeral %}{{ val|get_plural:"гвоздь,гвоздя,гвоздей" }}', 
            {'val': 10},
            '10 гвоздей')
        self.check_template_tag('get_plural', 
            '{% load pytils_numeral %}{{ val|get_plural:"гвоздь,гвоздя,гвоздей" }}', 
            {'val': 0},
            '0 гвоздей')
        self.check_template_tag('get_plural', 
            '{% load pytils_numeral %}{{ val|get_plural:"гвоздь,гвоздя,гвоздей,нет гвоздей" }}', 
            {'val': 0},
            'нет гвоздей')
    
    def testRublesFilter(self):
        self.check_template_tag('rubles', 
            '{% load pytils_numeral %}{{ val|rubles }}', 
            {'val': 10.1},
            'десять рублей десять копеек')
    
    def testInWordsFilter(self):
        self.check_template_tag('in_words', 
            '{% load pytils_numeral %}{{ val|in_words }}', 
            {'val': 21},
            'двадцать один')

        self.check_template_tag('in_words', 
            '{% load pytils_numeral %}{{ val|in_words:"NEUTER" }}', 
            {'val': 21},
            'двадцать одно')
    
    def testSumStringTag(self):
        self.check_template_tag('sum_string', 
            '{% load pytils_numeral %}{% sum_string val "MALE" "пример,пример,примеров" %}',
            {'val': 21},
            'двадцать один пример')
        self.check_template_tag('sum_string', 
            '{% load pytils_numeral %}{% sum_string val male variants %}',
            {
             'val': 21,
             'male':'MALE',
             'variants': ('пример','пример','примеров')
             },
            'двадцать один пример')

    # без отладки, если ошибка -- по умолчанию пустая строка
    def testChoosePluralError(self):
        self.check_template_tag('choose_plural_error', 
            '{% load pytils_numeral %}{{ val|choose_plural:"вариант" }}', 
            {'val': 1}, 
            '')


if __name__ == '__main__':
    import unittest
    unittest.main()



