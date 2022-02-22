# -*- coding: utf-8 -*-
"""
Unit tests for pytils' translit templatetags for Django web framework
"""

from . import helpers


class TranslitDefaultTestCase(helpers.TemplateTagTestCase):
    
    def testLoad(self):
        self.check_template_tag('{% load pytils_translit %}', {}, '')
    
    def testTranslifyFilter(self):
        self.check_template_tag(
            '{% load pytils_translit %}{{ val|translify }}',
            {'val': 'проверка'},
            'proverka'
        )
    
    def testDetranslifyFilter(self):
        self.check_template_tag(
            '{% load pytils_translit %}{{ val|detranslify }}',
            {'val': 'proverka'},
            'проверка'
        )

    def testSlugifyFilter(self):
        self.check_template_tag(
            '{% load pytils_translit %}{{ val|slugify }}',
            {'val': 'Проверка связи'},
            'proverka-svyazi'
        )

