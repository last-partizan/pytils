# -*- coding: utf-8 -*-
# License: GNU GPL2
# Author: Pythy <the.pythy@gmail.com>

__id__ = "$Id$"
__url__ = "$URL$"

import unittest
import pytils 

class ChoosePluralTestCase(unittest.TestCase):

    def setUp(self):
        self.variants = (u"гвоздь", u"гвоздя", u"гвоздей")

    def check_choose_plural(self, amount, estimated):
        self.assertEquals(pytils.numeral.choose_plural(amount, self.variants), estimated)
    
    def test_choose_plural(self):
        self.check_choose_plural(1, u"гвоздь")
        self.check_choose_plural(2, u"гвоздя")
        self.check_choose_plural(3, u"гвоздя")
        self.check_choose_plural(5, u"гвоздей")
        self.check_choose_plural(11, u"гвоздей")
        self.check_choose_plural(109, u"гвоздей")

class GetFloatRemainderTestCase(unittest.TestCase):

    def test_float_remainder(self):
        self.assertEquals(pytils.numeral._get_float_remainder(1.3), '3')
        self.assertEquals(pytils.numeral._get_float_remainder(2.35, 1), '4')
        self.assertEquals(pytils.numeral._get_float_remainder(123.1234567891), '123456789')
        self.assertEquals(pytils.numeral._get_float_remainder(2.353, 2), '35')
        self.assertEquals(pytils.numeral._get_float_remainder(0.01), '01')
        self.assertRaises(ValueError, pytils.numeral._get_float_remainder, 2.998, 2)

class RublesTestCase(unittest.TestCase):

    def test_rubles(self):
        self.assertEquals(pytils.numeral.rubles(10.01), u"десять рублей одна копейка")
        self.assertEquals(pytils.numeral.rubles(10.10), u"десять рублей десять копеек")
        self.assertEquals(pytils.numeral.rubles(2.353), u"два рубля тридцать пять копеек")
        self.assertEquals(pytils.numeral.rubles(2.998), u"три рубля")
        self.assertEquals(pytils.numeral.rubles(3), u"три рубля")
        self.assertEquals(pytils.numeral.rubles(3, True), u"три рубля ноль копеек")

class InWordsTestCase(unittest.TestCase):

    def test_int(self):
        self.assertEquals(pytils.numeral.in_words_int(10), u"десять")
        self.assertEquals(pytils.numeral.in_words_int(5), u"пять")
        self.assertEquals(pytils.numeral.in_words_int(102), u"сто два")
        self.assertEquals(pytils.numeral.in_words_int(3521), u"три тысячи пятьсот двадцать один")
        self.assertEquals(pytils.numeral.in_words_int(3500), u"три тысячи пятьсот")
        self.assertEquals(pytils.numeral.in_words_int(5231000), u"пять миллионов двести тридцать одна тысяча")
        self.assertRaises(AssertionError, pytils.numeral.in_words_int, 2.5)

    def test_float(self):
        self.assertEquals(pytils.numeral.in_words_float(10.0), u"десять целых ноль десятых")
        self.assertEquals(pytils.numeral.in_words_float(2.25), u"две целых двадцать пять сотых")
        self.assertEquals(pytils.numeral.in_words_float(0.01), u"ноль целых одна сотая")
        self.assertEquals(pytils.numeral.in_words_float(0.10), u"ноль целых одна десятая")
        self.assertRaises(AssertionError, pytils.numeral.in_words_float, 2)

    def test_common(self):
        self.assertEquals(pytils.numeral.in_words(10), u"десять")
        self.assertEquals(pytils.numeral.in_words(5), u"пять")
        self.assertEquals(pytils.numeral.in_words(102), u"сто два")
        self.assertEquals(pytils.numeral.in_words(3521), u"три тысячи пятьсот двадцать один")
        self.assertEquals(pytils.numeral.in_words(3500), u"три тысячи пятьсот")
        self.assertEquals(pytils.numeral.in_words(5231000), u"пять миллионов двести тридцать одна тысяча")
        self.assertEquals(pytils.numeral.in_words(10.0), u"десять целых ноль десятых")
        self.assertEquals(pytils.numeral.in_words(2.25), u"две целых двадцать пять сотых")
        self.assertEquals(pytils.numeral.in_words(0.01), u"ноль целых одна сотая")
        self.assertEquals(pytils.numeral.in_words(0.10), u"ноль целых одна десятая")
        self.assertRaises(AssertionError, pytils.numeral.in_words_float, '2')

class SumStringTestCase(unittest.TestCase):
    
    def setUp(self):
        self.variants_male = (u"гвоздь", u"гвоздя", u"гвоздей")
        self.variants_female = (u"шляпка", u"шляпки", u"шляпок")

    def ck_male(self, amount, estimated):
        self.assertEquals(pytils.numeral.sum_string(amount, 1, self.variants_male), estimated)

    def ck_female(self, amount, estimated):
        self.assertEquals(pytils.numeral.sum_string(amount, 2, self.variants_female), estimated)

    def test_sum_string(self):
        self.ck_male(10, u"десять гвоздей")
        self.ck_male(2, u"два гвоздя")
        self.ck_male(31, u"тридцать один гвоздь")
        self.ck_female(10, u"десять шляпок")
        self.ck_female(2, u"две шляпки")
        self.ck_female(31, u"тридцать одна шляпка")


if __name__ == '__main__':
    unittest.main()
