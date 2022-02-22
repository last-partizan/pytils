# -*- coding: utf-8 -*-
"""
Unit-tests for pytils.numeral
"""

import decimal
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
        self.variants = ("гвоздь", "гвоздя", "гвоздей")

    def checkChoosePlural(self, amount, estimated):
        """
        Checks choose_plural
        """
        self.assertEqual(
            pytils.numeral.choose_plural(amount, self.variants),
            estimated
        )
    
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

    def testChoosePluralNegativeBug9(self):
        """
        Test handling of negative numbers
        """
        self.checkChoosePlural(-5, "гвоздей")
        self.checkChoosePlural(-2, "гвоздя")

    def testChoosePluralExceptions(self):
        """
        Unit-test for testing choos_plural's exceptions
        """
        self.assertRaises(
            ValueError,
            pytils.numeral.choose_plural,
            25,
            "any,bene"
        )

    def testChoosePluralVariantsInStr(self):
        """
        Tests new-style variants
        """
        self.assertEqual(
            pytils.numeral.choose_plural(1, "гвоздь,гвоздя, гвоздей"),
            "гвоздь"
        )
        self.assertEqual(
            pytils.numeral.choose_plural(5, "гвоздь, гвоздя, гвоздей\, шпунтов"),
            "гвоздей, шпунтов"
        )


class GetPluralTestCase(unittest.TestCase):
    """
    Test case for get_plural
    """
    def testGetPlural(self):
        """
        Test regular get_plural
        """
        self.assertEqual(
            pytils.numeral.get_plural(1, "комментарий, комментария, комментариев"),
            "1 комментарий"
        )
        self.assertEqual(
            pytils.numeral.get_plural(0, "комментарий, комментария, комментариев"),
            "0 комментариев"
        )
        
    def testGetPluralAbsence(self):
        """
        Test get_plural with absence
        """
        self.assertEqual(
            pytils.numeral.get_plural(
                1,
                "комментарий, комментария, комментариев",
                "без комментариев"
            ),
            "1 комментарий"
        )
        self.assertEqual(
            pytils.numeral.get_plural(
                0,
                "комментарий, комментария, комментариев",
                "без комментариев"
            ),
            "без комментариев"
        )

    def testGetPluralLegacy(self):
        """
        Test _get_plural_legacy
        """
        self.assertEqual(
            pytils.numeral._get_plural_legacy(1, "комментарий, комментария, комментариев"),
            "1 комментарий"
        )
        self.assertEqual(
            pytils.numeral._get_plural_legacy(0, "комментарий, комментария, комментариев"),
            "0 комментариев"
        )
        self.assertEqual(
            pytils.numeral._get_plural_legacy(1, "комментарий, комментария, комментариев, без комментариев"),
            "1 комментарий"
        )
        self.assertEqual(
            pytils.numeral._get_plural_legacy(0, "комментарий, комментария, комментариев, без комментариев"),
            "без комментариев"
        )
        

class GetFloatRemainderTestCase(unittest.TestCase):
    """
    Test case for pytils.numeral._get_float_remainder
    """

    def testFloatRemainder(self):
        """
        Unit-test for _get_float_remainder
        """
        self.assertEqual(
            pytils.numeral._get_float_remainder(1.3),
            '3'
        )
        self.assertEqual(
            pytils.numeral._get_float_remainder(2.35, 1),
            '4'
        )
        self.assertEqual(
            pytils.numeral._get_float_remainder(123.1234567891),
            '123456789'
        )
        self.assertEqual(
            pytils.numeral._get_float_remainder(2.353, 2),
            '35'
        )
        self.assertEqual(
            pytils.numeral._get_float_remainder(0.01),
            '01'
        )
        self.assertEqual(
            pytils.numeral._get_float_remainder(5),
            '0'
        )

    def testFloatRemainderDecimal(self):
        """
        Unit-test for _get_float_remainder with decimal type
        """
        D = decimal.Decimal
        self.assertEqual(
            pytils.numeral._get_float_remainder(D("1.3")),
            '3'
        )
        self.assertEqual(
            pytils.numeral._get_float_remainder(D("2.35"), 1),
            '4'
        )
        self.assertEqual(
            pytils.numeral._get_float_remainder(D("123.1234567891")),
            '123456789'
        )
        self.assertEqual(
            pytils.numeral._get_float_remainder(D("2.353"), 2),
            '35'
        )
        self.assertEqual(
            pytils.numeral._get_float_remainder(D("0.01")),
            '01'
        )
        self.assertEqual(
            pytils.numeral._get_float_remainder(D("5")),
            '0'
        )

    def testFloatRemainderExceptions(self):
        """
        Unit-test for testing _get_float_remainder's exceptions
        """
        self.assertRaises(
            ValueError,
            pytils.numeral._get_float_remainder,
            2.998,
            2
        )
        self.assertRaises(
            ValueError,
            pytils.numeral._get_float_remainder,
            -1.23
        )


class RublesTestCase(unittest.TestCase):
    """
    Test case for pytils.numeral.rubles
    """

    def testRubles(self):
        """
        Unit-test for rubles
        """
        self.assertEqual(
            pytils.numeral.rubles(10.01),
            "десять рублей одна копейка"
        )
        self.assertEqual(
            pytils.numeral.rubles(10.10),
            "десять рублей десять копеек"
        )
        self.assertEqual(
            pytils.numeral.rubles(2.353),
            "два рубля тридцать пять копеек"
        )
        self.assertEqual(
            pytils.numeral.rubles(2.998),
            "три рубля"
        )
        self.assertEqual(
            pytils.numeral.rubles(3),
            "три рубля"
        )
        self.assertEqual(
            pytils.numeral.rubles(3, True),
            "три рубля ноль копеек"
        )

    def testRublesDecimal(self):
        """
        Test for rubles with decimal instead of float/integer
        """
        D = decimal.Decimal
        self.assertEqual(
            pytils.numeral.rubles(D("10.01")),
            "десять рублей одна копейка"
        )
        self.assertEqual(
            pytils.numeral.rubles(D("10.10")),
            "десять рублей десять копеек"
        )
        self.assertEqual(
            pytils.numeral.rubles(D("2.35")),
            "два рубля тридцать пять копеек"
        )
        self.assertEqual(
            pytils.numeral.rubles(D(3)),
            "три рубля"
        )
        self.assertEqual(
            pytils.numeral.rubles(D(3), True),
            "три рубля ноль копеек"
        )

    def testRublesExceptions(self):
        """
        Unit-test for testing rubles' exceptions
        """
        self.assertRaises(ValueError, pytils.numeral.rubles, -15)
        

class InWordsTestCase(unittest.TestCase):
    """
    Test case for pytils.numeral.in_words
    """

    def testInt(self):
        """
        Unit-test for in_words_int
        """
        self.assertEqual(pytils.numeral.in_words_int(0), "ноль")
        self.assertEqual(pytils.numeral.in_words_int(10), "десять")
        self.assertEqual(pytils.numeral.in_words_int(5), "пять")
        self.assertEqual(pytils.numeral.in_words_int(102), "сто два")
        self.assertEqual(pytils.numeral.in_words_int(3521), "три тысячи пятьсот двадцать один")
        self.assertEqual(pytils.numeral.in_words_int(3500), "три тысячи пятьсот")
        self.assertEqual(pytils.numeral.in_words_int(5231000), "пять миллионов двести тридцать одна тысяча")

    def testIntExceptions(self):
        """
        Unit-test for testing in_words_int's exceptions
        """
        self.assertRaises(ValueError, pytils.numeral.in_words_int, -3)

    def testFloat(self):
        """
        Unit-test for in_words_float
        """
        self.assertEqual(pytils.numeral.in_words_float(10.0), "десять целых ноль десятых")
        self.assertEqual(pytils.numeral.in_words_float(2.25), "две целых двадцать пять сотых")
        self.assertEqual(pytils.numeral.in_words_float(0.01), "ноль целых одна сотая")
        self.assertEqual(pytils.numeral.in_words_float(0.10), "ноль целых одна десятая")

    def testDecimal(self):
        """
        Unit-test for in_words_float with decimal type
        """
        D = decimal.Decimal
        self.assertEqual(
            pytils.numeral.in_words_float(D("10.0")),
            "десять целых ноль десятых"
        )
        self.assertEqual(
            pytils.numeral.in_words_float(D("2.25")),
            "две целых двадцать пять сотых"
        )
        self.assertEqual(
            pytils.numeral.in_words_float(D("0.01")),
            "ноль целых одна сотая"
        )
        # поскольку это Decimal, то здесь нет незначащих нулей
        # т.е. нули определяют точность, поэтому десять сотых,
        # а не одна десятая
        self.assertEqual(
            pytils.numeral.in_words_float(D("0.10")),
            "ноль целых десять сотых"
        )

    def testFloatExceptions(self):
        """
        Unit-test for testing in_words_float's exceptions
        """
        self.assertRaises(ValueError, pytils.numeral.in_words_float, -2.3)

    def testWithGenderOldStyle(self):
        """
        Unit-test for in_words_float with gender (old-style, i.e. ints)
        """
        self.assertEqual(pytils.numeral.in_words(21, 1), "двадцать один")
        self.assertEqual(pytils.numeral.in_words(21, 2), "двадцать одна")
        self.assertEqual(pytils.numeral.in_words(21, 3), "двадцать одно")
        # на дробные пол не должен влиять - всегда в женском роде
        self.assertEqual(pytils.numeral.in_words(21.0, 1), "двадцать одна целая ноль десятых")
        self.assertEqual(pytils.numeral.in_words(21.0, 2), "двадцать одна целая ноль десятых")
        self.assertEqual(pytils.numeral.in_words(21.0, 3), "двадцать одна целая ноль десятых")

    def testWithGender(self):
        """
        Unit-test for in_words_float with gender (old-style, i.e. ints)
        """
        self.assertEqual(
            pytils.numeral.in_words(21, pytils.numeral.MALE),
            "двадцать один"
        )
        self.assertEqual(
            pytils.numeral.in_words(21, pytils.numeral.FEMALE),
            "двадцать одна"
        )
        self.assertEqual(
            pytils.numeral.in_words(21, pytils.numeral.NEUTER),
            "двадцать одно"
        )
        # на дробные пол не должен влиять - всегда в женском роде
        self.assertEqual(
            pytils.numeral.in_words(21.0, pytils.numeral.MALE),
            "двадцать одна целая ноль десятых"
        )
        self.assertEqual(
            pytils.numeral.in_words(21.0, pytils.numeral.FEMALE),
            "двадцать одна целая ноль десятых"
        )
        self.assertEqual(
            pytils.numeral.in_words(21.0, pytils.numeral.NEUTER),
            "двадцать одна целая ноль десятых"
        )

    def testCommon(self):
        """
        Unit-test for general in_words
        """
        D = decimal.Decimal
        self.assertEqual(
            pytils.numeral.in_words(10),
            "десять"
        )
        self.assertEqual(
            pytils.numeral.in_words(5),
            "пять"
        )
        self.assertEqual(
            pytils.numeral.in_words(102),
            "сто два"
        )
        self.assertEqual(
            pytils.numeral.in_words(3521),
            "три тысячи пятьсот двадцать один"
        )
        self.assertEqual(
            pytils.numeral.in_words(3500),
            "три тысячи пятьсот"
        )
        self.assertEqual(
            pytils.numeral.in_words(5231000),
            "пять миллионов двести тридцать одна тысяча"
        )
        self.assertEqual(
            pytils.numeral.in_words(10.0),
            "десять целых ноль десятых"
        )
        self.assertEqual(
            pytils.numeral.in_words(2.25),
            "две целых двадцать пять сотых"
        )
        self.assertEqual(
            pytils.numeral.in_words(0.01),
            "ноль целых одна сотая"
        )
        self.assertEqual(
            pytils.numeral.in_words(0.10),
            "ноль целых одна десятая"
        )
        self.assertEqual(
            pytils.numeral.in_words(D("2.25")),
            "две целых двадцать пять сотых"
        )
        self.assertEqual(
            pytils.numeral.in_words(D("0.01")),
            "ноль целых одна сотая"
        )
        self.assertEqual(
            pytils.numeral.in_words(D("0.10")),
            "ноль целых десять сотых"
        )
        self.assertEqual(
            pytils.numeral.in_words(D("10")),
            "десять"
        )

    def testCommonExceptions(self):
        """
        Unit-test for testing in_words' exceptions
        """
        self.assertRaises(ValueError, pytils.numeral.in_words, -2)
        self.assertRaises(ValueError, pytils.numeral.in_words, -2.5)


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
        self.assertEqual(
            pytils.numeral.sum_string(amount, 1, self.variants_male),
            estimated
        )

    def ckMale(self, amount, estimated):
        """
        Checks sum_string with male gender
        """
        self.assertEqual(
            pytils.numeral.sum_string(amount, pytils.numeral.MALE, self.variants_male),
            estimated
        )

    def ckFemaleOldStyle(self, amount, estimated):
        """
        Checks sum_string with female gender wuth old-style genders (i.e. ints)
        """
        self.assertEqual(
            pytils.numeral.sum_string(amount, 2, self.variants_female),
            estimated
        )

    def ckFemale(self, amount, estimated):
        """
        Checks sum_string with female gender
        """
        self.assertEqual(
            pytils.numeral.sum_string(amount, pytils.numeral.FEMALE, self.variants_female),
            estimated
        )

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

        self.assertEqual(
            "одиннадцать негритят",
            pytils.numeral.sum_string(11, 1, "негритенок,негритенка,негритят")
        )

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

        self.assertEqual(
            "одиннадцать негритят",
            pytils.numeral.sum_string(11, pytils.numeral.MALE, "негритенок,негритенка,негритят")
        )

    def testSumStringExceptions(self):
        """
        Unit-test for testing sum_string's exceptions
        """
        self.assertRaises(
            ValueError,
            pytils.numeral.sum_string,
            -1,
            pytils.numeral.MALE,
            "any,bene,raba"
        )


if __name__ == '__main__':
    unittest.main()
