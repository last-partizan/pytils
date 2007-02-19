# -*- coding: utf-8 -*-
from pytils.test.templatetags import helpers

class NumeralDefaultTestCase(helpers.TemplateTagTestCase):

    def test_load(self):
        self.check_template_tag('load_tag', '{% load pytils_numeral %}', {}, '')
    
    def test_choose_plural_filter(self):
        self.check_template_tag('choose_plural', 
            '{% load pytils_numeral %}{{ val|choose_plural:"гвоздь,гвоздя,гвоздей" }}', 
            {'val': 10},
            'гвоздей')
    
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



