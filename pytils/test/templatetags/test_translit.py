# -*- coding: utf-8 -*-
from pytils.test.templatetags import helpers

class TranslitDefaultTestCase(helpers.TemplateTagTestCase):
    
    def test_load(self):
        self.check_template_tag('load_tag', '{% load pytils_translit %}', {}, '')
    
    def test_translify_filter(self):
        self.check_template_tag('translify_filter', 
            '{% load pytils_translit %}{{ val|translify }}', 
            {'val': 'проверка'}, 
            'proverka')
    
    def test_detranslify_filter(self):
        self.check_template_tag('detranslify_filter', 
            '{% load pytils_translit %}{{ val|detranslify }}', 
            {'val': 'proverka'}, 
            'проверка')        

    def test_slugify_filter(self):
        self.check_template_tag('slugify_filter', 
            '{% load pytils_translit %}{{ val|slugify }}', 
            {'val': 'Проверка связи'}, 
            'proverka-svyazi')
    
    # без отладки, если ошибка -- по умолчанию пустая строка
    def test_detranslify_error(self):
        self.check_template_tag('detranslify_error', 
            '{% load pytils_translit %}{{ val|detranslify }}', 
            {'val': 'Проверка связи'}, 
            '')


if __name__ == '__main__':
    import unittest
    unittest.main()