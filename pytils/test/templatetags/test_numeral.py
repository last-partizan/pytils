# -*- coding: utf-8 -*-
# PyTils - simple processing for russian strings
# Copyright (C) 2006-2007  Yury Yurevich
#
# http://gorod-omsk.ru/blog/pythy/projects/pytils/
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

    def test_load(self):
        self.check_template_tag('load_tag', '{% load pytils_numeral %}', {}, '')
    
    def test_choose_plural_filter(self):
        self.check_template_tag('choose_plural', 
            '{% load pytils_numeral %}{{ val|choose_plural:"гвоздь,гвоздя,гвоздей" }}', 
            {'val': 10},
            'гвоздей')

    def test_get_plural_filter(self):
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
    
    def test_rubles_filter(self):
        self.check_template_tag('rubles', 
            '{% load pytils_numeral %}{{ val|rubles }}', 
            {'val': 10.1},
            'десять рублей десять копеек')
    
    def test_in_words_filter(self):
        self.check_template_tag('in_words', 
            '{% load pytils_numeral %}{{ val|in_words }}', 
            {'val': 21},
            'двадцать один')

        self.check_template_tag('in_words', 
            '{% load pytils_numeral %}{{ val|in_words:"NEUTER" }}', 
            {'val': 21},
            'двадцать одно')
    
    def sum_string_tag(self):
        self.check_template_tag('sum_string', 
            '{% load pytils_numeral %}{% sum_string val "MALE" "пример,пример,примеров" %}',
            {'val': 21},
            'двадцать один пример')

    # без отладки, если ошибка -- по умолчанию пустая строка
    def test_choose_plural_error(self):
        self.check_template_tag('choose_plural_error', 
            '{% load pytils_numeral %}{{ val|choose_plural:"вариант" }}', 
            {'val': 1}, 
            '')


if __name__ == '__main__':
    import unittest
    unittest.main()



