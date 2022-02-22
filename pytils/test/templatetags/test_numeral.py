# -*- coding: utf-8 -*-
"""
Unit tests for pytils' numeral templatetags for Django web framework
"""

from . import helpers


class NumeralDefaultTestCase(helpers.TemplateTagTestCase):

    def testLoad(self):
        self.check_template_tag('{% load pytils_numeral %}', {}, '')
    
    def testChoosePluralFilter(self):
        self.check_template_tag(
            '{% load pytils_numeral %}{{ val|choose_plural:"гвоздь,гвоздя,гвоздей" }}',
            {'val': 10},
            'гвоздей'
        )

    def testGetPluralFilter(self):
        self.check_template_tag(
            '{% load pytils_numeral %}{{ val|get_plural:"гвоздь,гвоздя,гвоздей" }}',
            {'val': 10},
            '10 гвоздей'
        )

        self.check_template_tag(
            '{% load pytils_numeral %}{{ val|get_plural:"гвоздь,гвоздя,гвоздей" }}',
            {'val': 0},
            '0 гвоздей'
        )

        self.check_template_tag(
            '{% load pytils_numeral %}{{ val|get_plural:"гвоздь,гвоздя,гвоздей,нет гвоздей" }}',
            {'val': 0},
            'нет гвоздей'
        )
    
    def testRublesFilter(self):
        self.check_template_tag(
            '{% load pytils_numeral %}{{ val|rubles }}',
            {'val': 10.1},
            'десять рублей десять копеек'
        )
    
    def testInWordsFilter(self):
        self.check_template_tag(
            '{% load pytils_numeral %}{{ val|in_words }}',
            {'val': 21},
            'двадцать один'
        )

        self.check_template_tag(
            '{% load pytils_numeral %}{{ val|in_words:"NEUTER" }}',
            {'val': 21},
            'двадцать одно'
        )
    
    def testSumStringTag(self):
        self.check_template_tag(
            '{% load pytils_numeral %}{% sum_string val "MALE" "пример,пример,примеров" %}',
            {'val': 21},
            'двадцать один пример'
        )
        
        self.check_template_tag(
            '{% load pytils_numeral %}{% sum_string val male variants %}',
            {
             'val': 21,
             'male': 'MALE',
             'variants': ('пример', 'пример', 'примеров')
             },
            'двадцать один пример'
        )

    # без отладки, если ошибка -- по умолчанию пустая строка
    def testChoosePluralError(self):
        self.check_template_tag(
            '{% load pytils_numeral %}{{ val|choose_plural:"вариант" }}',
            {'val': 1},
            ''
        )


