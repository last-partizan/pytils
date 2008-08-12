# -*- coding: utf-8 -*-
# pytils - russian-specific string utils
# Copyright (C) 2006-2008  Yury Yurevich
#
# http://www.pyobject.ru/projects/pytils/
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

import unittest
import pytils

class ChoosePluralTestCase(unittest.TestCase):
    """
    Test case for pytils.numeral.choose_plural
    """

    def setUp(self):
        """
        Setting up environment for tests
        """
        self.variants = (u"гвоздь", u"гвоздя", u"гвоздей")

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
        self.checkChoosePlural(1, u"гвоздь")
        self.checkChoosePlural(2, u"гвоздя")
        self.checkChoosePlural(3, u"гвоздя")
        self.checkChoosePlural(5, u"гвоздей")
        self.checkChoosePlural(11, u"гвоздей")
        self.checkChoosePlural(109, u"гвоздей")
        self.checkChoosePlural(109l, u"гвоздей")

    def testChoosePluralExceptions(self):
        """
        Unit-test for testing choos_plural's exceptions
        """
        self.assertRaises(TypeError, pytils.numeral.choose_plural,
                          "25", u"any,bene,raba")
        self.assertRaises(TypeError, pytils.numeral.choose_plural,
                          25, 30)
        self.assertRaises(pytils.err.InputParameterError, pytils.numeral.choose_plural,
                          "25", u"any,bene,raba")
        self.assertRaises(pytils.err.InputParameterError, pytils.numeral.choose_plural,
                          25, 30)
        self.assertRaises(ValueError, pytils.numeral.choose_plural,
                          25, u"any,bene")
        self.assertRaises(ValueError, pytils.numeral.choose_plural,
                          -25, u"any,bene,raba")

    def testChoosePluralVariantsInStr(self):
        """
        Tests new-style variants
        """
        self.assertEquals(
            pytils.numeral.choose_plural(1,u"гвоздь,гвоздя, гвоздей"),
            u"гвоздь")
        self.assertEquals(
            pytils.numeral.choose_plural(5,u"гвоздь, гвоздя, гвоздей\, шпунтов"),
            u"гвоздей, шпунтов")

class GetPluralTestCase(unittest.TestCase):
    """
    Test case for get_plural
    """
    def testGetPlural(self):
        """
        Test regular get_plural
        """
        self.assertEquals(
            pytils.numeral.get_plural(1, u"комментарий, комментария, комментариев"),
            u"1 комментарий")
        self.assertEquals(
            pytils.numeral.get_plural(0, u"комментарий, комментария, комментариев"),
            u"0 комментариев")
        
    def testGetPluralAbsence(self):
        """
        Test get_plural with absence
        """
        self.assertEquals(
            pytils.numeral.get_plural(1, u"комментарий, комментария, комментариев",
                                      u"без комментариев"),
            u"1 комментарий")
        self.assertEquals(
            pytils.numeral.get_plural(0, u"комментарий, комментария, комментариев",
                                      u"без комментариев"),
            u"без комментариев")

    def testGetPluralLegacy(self):
        """
        Test _get_plural_legacy
        """
        self.assertEquals(
            pytils.numeral._get_plural_legacy(1, u"комментарий, комментария, комментариев"),
            u"1 комментарий")
        self.assertEquals(
            pytils.numeral._get_plural_legacy(0, u"комментарий, комментария, комментариев"),
            u"0 комментариев")
        self.assertEquals(
            pytils.numeral._get_plural_legacy(1, u"комментарий, комментария, комментариев, без комментариев"),
            u"1 комментарий")
        self.assertEquals(
            pytils.numeral._get_plural_legacy(0, u"комментарий, комментария, комментариев, без комментариев"),
            u"без комментариев")
        

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
                          u"десять рублей одна копейка")
        self.assertEquals(pytils.numeral.rubles(10.10),
                          u"десять рублей десять копеек")
        self.assertEquals(pytils.numeral.rubles(2.353),
                          u"два рубля тридцать пять копеек")
        self.assertEquals(pytils.numeral.rubles(2.998),
                          u"три рубля")
        self.assertEquals(pytils.numeral.rubles(3),
                          u"три рубля")
        self.assertEquals(pytils.numeral.rubles(3, True),
                          u"три рубля ноль копеек")
        self.assertEquals(pytils.numeral.rubles(3l),
                          u"три рубля")

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
        self.assertEquals(pytils.numeral.in_words_int(10), u"десять")
        self.assertEquals(pytils.numeral.in_words_int(5), u"пять")
        self.assertEquals(pytils.numeral.in_words_int(102), u"сто два")
        self.assertEquals(pytils.numeral.in_words_int(3521),
                          u"три тысячи пятьсот двадцать один")
        self.assertEquals(pytils.numeral.in_words_int(3500),
                          u"три тысячи пятьсот")
        self.assertEquals(pytils.numeral.in_words_int(5231000),
                          u"пять миллионов двести тридцать одна тысяча")
        self.assertEquals(pytils.numeral.in_words_int(10l), u"десять")

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
                          u"десять целых ноль десятых")
        self.assertEquals(pytils.numeral.in_words_float(2.25),
                          u"две целых двадцать пять сотых")
        self.assertEquals(pytils.numeral.in_words_float(0.01),
                          u"ноль целых одна сотая")
        self.assertEquals(pytils.numeral.in_words_float(0.10),
                          u"ноль целых одна десятая")

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
                          u"двадцать один")
        self.assertEquals(pytils.numeral.in_words(21, 2),
                          u"двадцать одна")
        self.assertEquals(pytils.numeral.in_words(21, 3),
                          u"двадцать одно")
        # на дробные пол не должен влиять - всегда в женском роде
        self.assertEquals(pytils.numeral.in_words(21.0, 1),
                          u"двадцать одна целая ноль десятых")
        self.assertEquals(pytils.numeral.in_words(21.0, 2),
                          u"двадцать одна целая ноль десятых")
        self.assertEquals(pytils.numeral.in_words(21.0, 3),
                          u"двадцать одна целая ноль десятых")
        self.assertEquals(pytils.numeral.in_words(21l, 1),
                          u"двадцать один")

    def testWithGender(self):
        """
        Unit-test for in_words_float with gender (old-style, i.e. ints)
        """
        self.assertEquals(pytils.numeral.in_words(21, pytils.numeral.MALE),
                          u"двадцать один")
        self.assertEquals(pytils.numeral.in_words(21, pytils.numeral.FEMALE),
                          u"двадцать одна")
        self.assertEquals(pytils.numeral.in_words(21, pytils.numeral.NEUTER),
                          u"двадцать одно")
        # на дробные пол не должен влиять - всегда в женском роде
        self.assertEquals(pytils.numeral.in_words(21.0, pytils.numeral.MALE),
                          u"двадцать одна целая ноль десятых")
        self.assertEquals(pytils.numeral.in_words(21.0, pytils.numeral.FEMALE),
                          u"двадцать одна целая ноль десятых")
        self.assertEquals(pytils.numeral.in_words(21.0, pytils.numeral.NEUTER),
                          u"двадцать одна целая ноль десятых")
        self.assertEquals(pytils.numeral.in_words(21l, pytils.numeral.MALE),
                          u"двадцать один")


    def testCommon(self):
        """
        Unit-test for general in_words
        """                
        self.assertEquals(pytils.numeral.in_words(10), u"десять")
        self.assertEquals(pytils.numeral.in_words(5), u"пять")
        self.assertEquals(pytils.numeral.in_words(102), u"сто два")
        self.assertEquals(pytils.numeral.in_words(3521),
                          u"три тысячи пятьсот двадцать один")
        self.assertEquals(pytils.numeral.in_words(3500),
                          u"три тысячи пятьсот")
        self.assertEquals(pytils.numeral.in_words(5231000),
                          u"пять миллионов двести тридцать одна тысяча")
        self.assertEquals(pytils.numeral.in_words(10.0),
                          u"десять целых ноль десятых")
        self.assertEquals(pytils.numeral.in_words(2.25),
                          u"две целых двадцать пять сотых")
        self.assertEquals(pytils.numeral.in_words(0.01),
                          u"ноль целых одна сотая")
        self.assertEquals(pytils.numeral.in_words(0.10),
                          u"ноль целых одна десятая")
        self.assertEquals(pytils.numeral.in_words(10l), u"десять")

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
        self.variants_male = (u"гвоздь", u"гвоздя", u"гвоздей")
        self.variants_female = (u"шляпка", u"шляпки", u"шляпок")

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
        self.ckMaleOldStyle(10, u"десять гвоздей")
        self.ckMaleOldStyle(2, u"два гвоздя")
        self.ckMaleOldStyle(31, u"тридцать один гвоздь")
        self.ckFemaleOldStyle(10, u"десять шляпок")
        self.ckFemaleOldStyle(2, u"две шляпки")
        self.ckFemaleOldStyle(31, u"тридцать одна шляпка")
        
        self.ckFemaleOldStyle(31l, u"тридцать одна шляпка")

        self.assertEquals(u"одиннадцать негритят",
                          pytils.numeral.sum_string(
                              11,
                              1,
                              u"негритенок,негритенка,негритят"
                              ))

    def testSumString(self):
        """
        Unit-test for sum_string
        """
        self.ckMale(10, u"десять гвоздей")
        self.ckMale(2, u"два гвоздя")
        self.ckMale(31, u"тридцать один гвоздь")
        self.ckFemale(10, u"десять шляпок")
        self.ckFemale(2, u"две шляпки")
        self.ckFemale(31, u"тридцать одна шляпка")
        
        self.ckFemale(31l, u"тридцать одна шляпка")

        self.assertEquals(u"одиннадцать негритят",
                          pytils.numeral.sum_string(
                              11,
                              pytils.numeral.MALE,
                              u"негритенок,негритенка,негритят"
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
                                      -1, pytils.numeral.MALE, u"any,bene,raba")

if __name__ == '__main__':
    unittest.main()
