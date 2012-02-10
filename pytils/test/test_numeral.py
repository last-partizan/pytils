# -*- coding: utf-8 -*-
# pytils - russian-specific string utils
# Copyright (C) 2006-2009  Yury Yurevich
#
# http://pyobject.ru/projects/pytils/
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
Unit-tests for pytils.numeral
"""
from __future__ import print_function, absolute_import, division, unicode_literals

import unittest
import decimal
import six
import pytils

class ChoosePluralTestCase(unittest.TestCase):
    """
    Test case for pytils.numeral.choose_plural
    """

    def setUp(self):
        """
        Setting up environment for tests
        """
        self.variants = ("гвоздь", "гвоздя", "гвоздей")

    def checkChoosePlural(self, amount, estimated):
        """
        Checks choose_plural
        """
        self.assertEquals(pytils.numeral.choose_plural(amount, self.variants),
                          estimated)

    def testChoosePlural(self):
        """
        Unit-test for choose_plural
        """
        self.checkChoosePlural(1, "гвоздь")
        self.checkChoosePlural(2, "гвоздя")
        self.checkChoosePlural(3, "гвоздя")
        self.checkChoosePlural(5, "гвоздей")
        self.checkChoosePlural(11, "гвоздей")
        self.checkChoosePlural(109, "гвоздей")
        if not six.PY3:
            self.checkChoosePlural(long(109), "гвоздей")

    def testChoosePluralExceptions(self):
        """
        Unit-test for testing choos_plural's exceptions
        """
        self.assertRaises(TypeError, pytils.numeral.choose_plural,
                          "25", "any,bene,raba")
        self.assertRaises(TypeError, pytils.numeral.choose_plural,
                          25, 30)
        self.assertRaises(pytils.err.InputParameterError, pytils.numeral.choose_plural,
                          "25", "any,bene,raba")
        self.assertRaises(pytils.err.InputParameterError, pytils.numeral.choose_plural,
                          25, 30)
        self.assertRaises(ValueError, pytils.numeral.choose_plural,
                          25, "any,bene")
        self.assertRaises(ValueError, pytils.numeral.choose_plural,
                          -25, "any,bene,raba")

    def testChoosePluralVariantsInStr(self):
        """
        Tests new-style variants
        """
        self.assertEquals(
            pytils.numeral.choose_plural(1,"гвоздь,гвоздя, гвоздей"),
            "гвоздь")
        self.assertEquals(
            pytils.numeral.choose_plural(5,"гвоздь, гвоздя, гвоздей\, шпунтов"),
            "гвоздей, шпунтов")

class GetPluralTestCase(unittest.TestCase):
    """
    Test case for get_plural
    """
    def testGetPlural(self):
        """
        Test regular get_plural
        """
        self.assertEquals(
            pytils.numeral.get_plural(1, "комментарий, комментария, комментариев"),
            "1 комментарий")
        self.assertEquals(
            pytils.numeral.get_plural(0, "комментарий, комментария, комментариев"),
            "0 комментариев")

    def testGetPluralAbsence(self):
        """
        Test get_plural with absence
        """
        self.assertEquals(
            pytils.numeral.get_plural(1, "комментарий, комментария, комментариев",
                                      "без комментариев"),
            "1 комментарий")
        self.assertEquals(
            pytils.numeral.get_plural(0, "комментарий, комментария, комментариев",
                                      "без комментариев"),
            "без комментариев")

    def testGetPluralLegacy(self):
        """
        Test _get_plural_legacy
        """
        self.assertEquals(
            pytils.numeral._get_plural_legacy(1, "комментарий, комментария, комментариев"),
            "1 комментарий")
        self.assertEquals(
            pytils.numeral._get_plural_legacy(0, "комментарий, комментария, комментариев"),
            "0 комментариев")
        self.assertEquals(
            pytils.numeral._get_plural_legacy(1, "комментарий, комментария, комментариев, без комментариев"),
            "1 комментарий")
        self.assertEquals(
            pytils.numeral._get_plural_legacy(0, "комментарий, комментария, комментариев, без комментариев"),
            "без комментариев")


class GetFloatRemainderTestCase(unittest.TestCase):
    """
    Test case for pytils.numeral._get_float_remainder
    """

    def testFloatRemainder(self):
        """
        Unit-test for _get_float_remainder
        """
        self.assertEquals(pytils.numeral._get_float_remainder(1.3),
                          '3')
        self.assertEquals(pytils.numeral._get_float_remainder(2.35, 1),
                          '4')
        self.assertEquals(pytils.numeral._get_float_remainder(123.1234567891),
                          '123456789')
        self.assertEquals(pytils.numeral._get_float_remainder(2.353, 2),
                          '35')
        self.assertEquals(pytils.numeral._get_float_remainder(0.01),
                          '01')
        self.assertEquals(pytils.numeral._get_float_remainder(5),
                          '0')

    def testFloatRemainderDecimal(self):
        """
        Unit-test for _get_float_remainder with decimal type
        """
        D = decimal.Decimal
        self.assertEquals(pytils.numeral._get_float_remainder(D("1.3")),
                          '3')
        self.assertEquals(pytils.numeral._get_float_remainder(D("2.35"), 1),
                          '4')
        self.assertEquals(pytils.numeral._get_float_remainder(D("123.1234567891")),
                          '123456789')
        self.assertEquals(pytils.numeral._get_float_remainder(D("2.353"), 2),
                          '35')
        self.assertEquals(pytils.numeral._get_float_remainder(D("0.01")),
                          '01')
        self.assertEquals(pytils.numeral._get_float_remainder(D("5")),
                          '0')

    def testFloatRemainderExceptions(self):
        """
        Unit-test for testing _get_float_remainder's exceptions
        """
        self.assertRaises(ValueError, pytils.numeral._get_float_remainder,
                          2.998, 2)
        self.assertRaises(TypeError, pytils.numeral._get_float_remainder, "1.23")
        self.assertRaises(pytils.err.InputParameterError, pytils.numeral._get_float_remainder, "1.23")
        self.assertRaises(ValueError, pytils.numeral._get_float_remainder, -1.23)

class RublesTestCase(unittest.TestCase):
    """
    Test case for pytils.numeral.rubles
    """

    def testRubles(self):
        """
        Unit-test for rubles
        """
        self.assertEquals(pytils.numeral.rubles(10.01),
                          "десять рублей одна копейка")
        self.assertEquals(pytils.numeral.rubles(10.10),
                          "десять рублей десять копеек")
        self.assertEquals(pytils.numeral.rubles(2.353),
                          "два рубля тридцать пять копеек")
        self.assertEquals(pytils.numeral.rubles(2.998),
                          "три рубля")
        self.assertEquals(pytils.numeral.rubles(3),
                          "три рубля")
        self.assertEquals(pytils.numeral.rubles(3, True),
                          "три рубля ноль копеек")
        if not six.PY3:
            self.assertEquals(pytils.numeral.rubles(long(3)),
                          "три рубля")

    def testRublesDecimal(self):
        """
        Test for rubles with decimal instead of float/integer
        """
        D = decimal.Decimal
        self.assertEquals(pytils.numeral.rubles(D("10.01")),
                          "десять рублей одна копейка")
        self.assertEquals(pytils.numeral.rubles(D("10.10")),
                          "десять рублей десять копеек")
        self.assertEquals(pytils.numeral.rubles(D("2.35")),
                          "два рубля тридцать пять копеек")
        self.assertEquals(pytils.numeral.rubles(D(3)),
                          "три рубля")
        self.assertEquals(pytils.numeral.rubles(D(3), True),
                          "три рубля ноль копеек")

    def testRublesExceptions(self):
        """
        Unit-test for testing rubles' exceptions
        """
        self.assertRaises(TypeError, pytils.numeral.rubles, "3")
        self.assertRaises(pytils.err.InputParameterError, pytils.numeral.rubles, "3")
        self.assertRaises(ValueError, pytils.numeral.rubles, -15)


class InWordsTestCase(unittest.TestCase):
    """
    Test case for pytils.numeral.in_words
    """

    def testInt(self):
        """
        Unit-test for in_words_int
        """
        self.assertEquals(pytils.numeral.in_words_int(10), "десять")
        self.assertEquals(pytils.numeral.in_words_int(5), "пять")
        self.assertEquals(pytils.numeral.in_words_int(102), "сто два")
        self.assertEquals(pytils.numeral.in_words_int(3521),
                          "три тысячи пятьсот двадцать один")
        self.assertEquals(pytils.numeral.in_words_int(3500),
                          "три тысячи пятьсот")
        self.assertEquals(pytils.numeral.in_words_int(5231000),
                          "пять миллионов двести тридцать одна тысяча")
        if not six.PY3:
            self.assertEquals(pytils.numeral.in_words_int(long(10)), "десять")

    def testIntExceptions(self):
        """
        Unit-test for testing in_words_int's exceptions
        """
        self.assertRaises(TypeError, pytils.numeral.in_words_int, 2.5)
        self.assertRaises(pytils.err.InputParameterError, pytils.numeral.in_words_int, 2.5)
        self.assertRaises(ValueError, pytils.numeral.in_words_int, -3)

    def testFloat(self):
        """
        Unit-test for in_words_float
        """
        self.assertEquals(pytils.numeral.in_words_float(10.0),
                          "десять целых ноль десятых")
        self.assertEquals(pytils.numeral.in_words_float(2.25),
                          "две целых двадцать пять сотых")
        self.assertEquals(pytils.numeral.in_words_float(0.01),
                          "ноль целых одна сотая")
        self.assertEquals(pytils.numeral.in_words_float(0.10),
                          "ноль целых одна десятая")

    def testDecimal(self):
        """
        Unit-test for in_words_float with decimal type
        """
        D = decimal.Decimal
        self.assertEquals(pytils.numeral.in_words_float(D("10.0")),
                          "десять целых ноль десятых")
        self.assertEquals(pytils.numeral.in_words_float(D("2.25")),
                          "две целых двадцать пять сотых")
        self.assertEquals(pytils.numeral.in_words_float(D("0.01")),
                          "ноль целых одна сотая")
        # поскольку это Decimal, то здесь нет незначащих нулей
        # т.е. нули определяют точность, поэтому десять сотых,
        # а не одна десятая
        self.assertEquals(pytils.numeral.in_words_float(D("0.10")),
                          "ноль целых десять сотых")

    def testFloatExceptions(self):
        """
        Unit-test for testing in_words_float's exceptions
        """
        self.assertRaises(TypeError, pytils.numeral.in_words_float, '2')
        self.assertRaises(TypeError, pytils.numeral.in_words_float, 2)
        self.assertRaises(pytils.err.InputParameterError, pytils.numeral.in_words_float, '2')
        self.assertRaises(pytils.err.InputParameterError, pytils.numeral.in_words_float, 2)
        self.assertRaises(ValueError, pytils.numeral.in_words_float, -2.3)

    def testWithGenderOldStyle(self):
        """
        Unit-test for in_words_float with gender (old-style, i.e. ints)
        """
        self.assertEquals(pytils.numeral.in_words(21, 1),
                          "двадцать один")
        self.assertEquals(pytils.numeral.in_words(21, 2),
                          "двадцать одна")
        self.assertEquals(pytils.numeral.in_words(21, 3),
                          "двадцать одно")
        # на дробные пол не должен влиять - всегда в женском роде
        self.assertEquals(pytils.numeral.in_words(21.0, 1),
                          "двадцать одна целая ноль десятых")
        self.assertEquals(pytils.numeral.in_words(21.0, 2),
                          "двадцать одна целая ноль десятых")
        self.assertEquals(pytils.numeral.in_words(21.0, 3),
                          "двадцать одна целая ноль десятых")
        if not six.PY3:
            self.assertEquals(pytils.numeral.in_words(long(21), 1),
                          "двадцать один")

    def testWithGender(self):
        """
        Unit-test for in_words_float with gender (old-style, i.e. ints)
        """
        self.assertEquals(pytils.numeral.in_words(21, pytils.numeral.MALE),
                          "двадцать один")
        self.assertEquals(pytils.numeral.in_words(21, pytils.numeral.FEMALE),
                          "двадцать одна")
        self.assertEquals(pytils.numeral.in_words(21, pytils.numeral.NEUTER),
                          "двадцать одно")
        # на дробные пол не должен влиять - всегда в женском роде
        self.assertEquals(pytils.numeral.in_words(21.0, pytils.numeral.MALE),
                          "двадцать одна целая ноль десятых")
        self.assertEquals(pytils.numeral.in_words(21.0, pytils.numeral.FEMALE),
                          "двадцать одна целая ноль десятых")
        self.assertEquals(pytils.numeral.in_words(21.0, pytils.numeral.NEUTER),
                          "двадцать одна целая ноль десятых")
        if not six.PY3:
            self.assertEquals(pytils.numeral.in_words(long(21), pytils.numeral.MALE),
                          "двадцать один")


    def testCommon(self):
        """
        Unit-test for general in_words
        """
        D = decimal.Decimal
        self.assertEquals(pytils.numeral.in_words(10), "десять")
        self.assertEquals(pytils.numeral.in_words(5), "пять")
        self.assertEquals(pytils.numeral.in_words(102), "сто два")
        self.assertEquals(pytils.numeral.in_words(3521),
                          "три тысячи пятьсот двадцать один")
        self.assertEquals(pytils.numeral.in_words(3500),
                          "три тысячи пятьсот")
        self.assertEquals(pytils.numeral.in_words(5231000),
                          "пять миллионов двести тридцать одна тысяча")
        self.assertEquals(pytils.numeral.in_words(10.0),
                          "десять целых ноль десятых")
        self.assertEquals(pytils.numeral.in_words(2.25),
                          "две целых двадцать пять сотых")
        self.assertEquals(pytils.numeral.in_words(0.01),
                          "ноль целых одна сотая")
        self.assertEquals(pytils.numeral.in_words(0.10),
                          "ноль целых одна десятая")
        if not six.PY3:
            self.assertEquals(pytils.numeral.in_words(long(10)), "десять")
        self.assertEquals(pytils.numeral.in_words(D("2.25")),
                          "две целых двадцать пять сотых")
        self.assertEquals(pytils.numeral.in_words(D("0.01")),
                          "ноль целых одна сотая")
        self.assertEquals(pytils.numeral.in_words(D("0.10")),
                          "ноль целых десять сотых")
        self.assertEquals(pytils.numeral.in_words(D("10")), "десять")

    def testCommonExceptions(self):
        """
        Unit-test for testing in_words' exceptions
        """
        self.assertRaises(TypeError, pytils.numeral.in_words, "0.2")
        self.assertRaises(TypeError, pytils.numeral.in_words, 0.2, "1")
        self.assertRaises(TypeError, pytils.numeral.in_words, 0.2, 5)
        self.assertRaises(pytils.err.InputParameterError, pytils.numeral.in_words, "0.2")
        self.assertRaises(pytils.err.InputParameterError, pytils.numeral.in_words, 0.2, "1")
        self.assertRaises(pytils.err.InputParameterError, pytils.numeral.in_words, 0.2, 5)
        self.assertRaises(ValueError, pytils.numeral.in_words, -2)


class SumStringTestCase(unittest.TestCase):
    """
    Test case for pytils.numeral.sum_string
    """

    def setUp(self):
        """
        Setting up environment for tests
        """
        self.variants_male = ("гвоздь", "гвоздя", "гвоздей")
        self.variants_female = ("шляпка", "шляпки", "шляпок")

    def ckMaleOldStyle(self, amount, estimated):
        """
        Checks sum_string with male gender with old-style genders (i.e. ints)
        """
        self.assertEquals(pytils.numeral.sum_string(amount,
                                                    1,
                                                    self.variants_male),
                          estimated)

    def ckMale(self, amount, estimated):
        """
        Checks sum_string with male gender
        """
        self.assertEquals(pytils.numeral.sum_string(amount,
                                                    pytils.numeral.MALE,
                                                    self.variants_male),
                          estimated)


    def ckFemaleOldStyle(self, amount, estimated):
        """
        Checks sum_string with female gender wuth old-style genders (i.e. ints)
        """
        self.assertEquals(pytils.numeral.sum_string(amount,
                                                    2,
                                                    self.variants_female),
                          estimated)

    def ckFemale(self, amount, estimated):
        """
        Checks sum_string with female gender
        """
        self.assertEquals(pytils.numeral.sum_string(amount,
                                                    pytils.numeral.FEMALE,
                                                    self.variants_female),
                          estimated)

    def testSumStringOldStyleGender(self):
        """
        Unit-test for sum_string with old-style genders
        """
        self.ckMaleOldStyle(10, "десять гвоздей")
        self.ckMaleOldStyle(2, "два гвоздя")
        self.ckMaleOldStyle(31, "тридцать один гвоздь")
        self.ckFemaleOldStyle(10, "десять шляпок")
        self.ckFemaleOldStyle(2, "две шляпки")
        self.ckFemaleOldStyle(31, "тридцать одна шляпка")

        if not six.PY3:
            self.ckFemaleOldStyle(long(31), "тридцать одна шляпка")

        self.assertEquals("одиннадцать негритят",
                          pytils.numeral.sum_string(
                              11,
                              1,
                              "негритенок,негритенка,негритят"
                              ))

    def testSumString(self):
        """
        Unit-test for sum_string
        """
        self.ckMale(10, "десять гвоздей")
        self.ckMale(2, "два гвоздя")
        self.ckMale(31, "тридцать один гвоздь")
        self.ckFemale(10, "десять шляпок")
        self.ckFemale(2, "две шляпки")
        self.ckFemale(31, "тридцать одна шляпка")

        if not six.PY3:
            self.ckFemale(long(31), "тридцать одна шляпка")

        self.assertEquals("одиннадцать негритят",
                          pytils.numeral.sum_string(
                              11,
                              pytils.numeral.MALE,
                              "негритенок,негритенка,негритят"
                              ))

    def testSumStringExceptions(self):
        """
        Unit-test for testing sum_string's exceptions
        """
        self.assertRaises(TypeError, pytils.numeral.sum_string,
                                      "1", 1)
        self.assertRaises(TypeError, pytils.numeral.sum_string,
                                      1, "1")
        self.assertRaises(TypeError, pytils.numeral.sum_string,
                                      1, "1", 23)
        self.assertRaises(TypeError, pytils.numeral.sum_string,
                                      1, pytils.numeral.MALE, (23,24,25))
        self.assertRaises(TypeError, pytils.numeral.sum_string,
                                      1, pytils.numeral.MALE, (23,))
        self.assertRaises(pytils.err.InputParameterError, pytils.numeral.sum_string,
                                      "1", 1)
        self.assertRaises(pytils.err.InputParameterError, pytils.numeral.sum_string,
                                      1, "1")
        self.assertRaises(pytils.err.InputParameterError, pytils.numeral.sum_string,
                                      1, "1", 23)
        self.assertRaises(pytils.err.InputParameterError, pytils.numeral.sum_string,
                                      1, pytils.numeral.MALE, (23,24,25))
        self.assertRaises(pytils.err.InputParameterError, pytils.numeral.sum_string,
                                      1, pytils.numeral.MALE, (23,))
        self.assertRaises(ValueError, pytils.numeral.sum_string,
                                      -1, pytils.numeral.MALE, "any,bene,raba")

if __name__ == '__main__':
    unittest.main()
