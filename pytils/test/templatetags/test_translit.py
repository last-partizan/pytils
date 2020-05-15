# -*- coding: utf-8 -*-
"""
Unit tests for pytils' translit templatetags for Django web framework
"""

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


if __name__ == '__main__':
    import unittest
    unittest.main()
