# -*- coding: utf-8 -*-
# License: GNU GPL2
# Author: Pythy <the.pythy@gmail.com>

__id__ = "$Id$"
__url__ = "$URL$"

import unittest

import pytils

class TranslitTestCase(unittest.TestCase):

    def ck_transl(self, in_, out_):
        self.assertEquals(pytils.translit.translify(in_), out_)

    def ck_detransl(self, in_, out_):
        self.assertEquals(pytils.translit.detranslify(in_), out_)

    def ck_slug(self, in_, out_):
        self.assertEquals(pytils.translit.slugify(in_), out_)

    def test_transliteration(self):
        self.ck_transl(u"тест", 'test')
        self.ck_transl(u"проверка", 'proverka')
        self.ck_transl(u"транслит", 'translit')
        self.ck_transl(u"правда ли это", 'pravda li eto')

    def test_detransliteration(self):
        self.ck_detransl('test', u"тест")
        self.ck_detransl('proverka', u"проверка")
        self.ck_detransl('translit', u"транслит")

    def test_slug(self):
        self.ck_slug(u"ТеСт", 'test')
        self.ck_slug(u"Проверка связи", 'proverka-svyazi')
        self.ck_slug(u"me&you", 'me-and-you')
        self.ck_slug(u"и еще один тест", 'i-esche-odin-test')

if __name__ == '__main__':
    unittest.main()
