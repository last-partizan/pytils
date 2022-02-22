# -*- coding: utf-8 -*-
"""
Unit-tests for pytils.translit
"""

import unittest

import pytils


class TranslitTestCase(unittest.TestCase):
    """
    Test case for pytils.translit
    """

    def ckTransl(self, in_, out_):
        """
        Checks translify
        """
        self.assertEqual(pytils.translit.translify(in_), out_)

    def ckDetransl(self, in_, out_):
        """
        Checks detranslify
        """
        self.assertEqual(pytils.translit.detranslify(in_), out_)

    def ckSlug(self, in_, out_):
        """
        Checks slugify
        """
        self.assertEqual(pytils.translit.slugify(in_), out_)

    def testTransliteration(self):
        """
        Unit-test for transliterations
        """
        self.ckTransl("тест", 'test')
        self.ckTransl("проверка", 'proverka')
        self.ckTransl("транслит", 'translit')
        self.ckTransl("правда ли это", 'pravda li eto')
        self.ckTransl("Щука", 'Schuka')

    def testTransliterationExceptions(self):
        """
        Unit-test for testing translify's exceptions
        """
        self.assertRaises(ValueError, pytils.translit.translify, '\u00bfHabla espa\u00f1ol?')

    def testDetransliteration(self):
        """
        Unit-test for detransliterations
        """
        self.ckDetransl('test', "тест")
        self.ckDetransl('proverka', "проверка")
        self.ckDetransl('translit', "транслит")
        self.ckDetransl('SCHuka', "Щука")
        self.ckDetransl('Schuka', "Щука")

    def testSlug(self):
        """
        Unit-test for slugs
        """
        self.ckSlug("ТеСт", 'test')
        self.ckSlug("Проверка связи", 'proverka-svyazi')
        self.ckSlug("me&you", 'me-and-you')
        self.ckSlug("и еще один тест", 'i-esche-odin-test')

    def testTranslifyAdditionalUnicodeSymbols(self):
        """
        Unit-test for testing additional unicode symbols
        """
        self.ckTransl("«Вот так вот»", '"Vot tak vot"')
        self.ckTransl("‘Или вот так’", "'Ili vot tak'")
        self.ckTransl("– Да…", "- Da...")

    def testSlugifyIssue10(self):
        """
        Unit-test for testing that bug#10 fixed
        """
        self.ckSlug("Проверка связи…", 'proverka-svyazi')
        self.ckSlug("Проверка\x0aсвязи 2", 'proverka-svyazi-2')
        self.ckSlug("Проверка\201связи 3", 'proverkasvyazi-3')

    def testSlugifyIssue15(self):
        """
        Unit-test for testing that bug#15 fixed
        """
        self.ckSlug("World of Warcraft", "world-of-warcraft")

    def testAdditionalDashesAndQuotes(self):
        """
        Unit-test for testing additional dashes (figure and em-dash)
        and quotes
        """
        self.ckSlug("Юнит-тесты — наше всё", 'yunit-testyi---nashe-vsyo')
        self.ckSlug("Юнит-тесты ‒ наше всё", 'yunit-testyi---nashe-vsyo')
        self.ckSlug("95−34", '95-34')
        self.ckTransl("Двигатель “Pratt&Whitney”", 'Dvigatel\' "Pratt&Whitney"')


if __name__ == '__main__':
    unittest.main()
