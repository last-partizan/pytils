# -*- coding: utf-8 -*-
"""
Unit-tests for pytils.typo
"""

import os
import unittest

from pytils import typo


def cb_testrule(x):
    return x


class HelpersTestCase(unittest.TestCase):
    """
    Test case for pytils.typo helpers
    """
    def testGetRuleByName(self):
        """
        unit-test for pytils.typo._get_rule_by_name
        """
        self.assertTrue(
            callable(typo._get_rule_by_name('testrule'))
        )
        self.assertEqual(
            'rl_testrule',
            typo._get_rule_by_name('testrule').__name__
        )
    
    def testResolveRule(self):
        """
        unit-test for pytils.typo._resolve_rule
        """
        self.assertTrue(
            callable(typo._resolve_rule_name('testrule')[1])
        )
        self.assertTrue(
            callable(typo._resolve_rule_name(cb_testrule)[1])
        )
        self.assertEqual(
            'testrule',
            typo._resolve_rule_name('testrule')[0]
        )
        self.assertEqual(
            'cb_testrule',
            typo._resolve_rule_name(cb_testrule)[0]
        )

    def testResolveRuleWithForcedName(self):
        """
        unit-test for pytils.typo._resolve_rule with forced_name arg
        """
        self.assertTrue(
            callable(typo._resolve_rule_name('testrule', 'newrule')[1])
        )
        self.assertTrue(
            callable(typo._resolve_rule_name(cb_testrule, 'newrule')[1])
        )
        self.assertEqual(
            'newrule',
            typo._resolve_rule_name('testrule', 'newrule')[0]
        )
        self.assertEqual(
            'newrule',
            typo._resolve_rule_name(cb_testrule, 'newrule')[0]
        )


class TypographyApplierTestCase(unittest.TestCase):
    """
    Test case for typography rule applier pytils.typo.Typography
    """
    def testExpandEmptyArgs(self):
        self.assertEqual(
            {},
            typo.Typography().rules
        )
        self.assertEqual(
            [],
            typo.Typography().rules_names
        )
    
    def testExpandSimpleStrArgs(self):
        self.assertEqual(
            {'testrule': typo.rl_testrule},
            typo.Typography('testrule').rules
        )
        self.assertEqual(
            ['testrule'],
            typo.Typography('testrule').rules_names
        )
    
    def testExpandDictStrArgs(self):
        self.assertEqual(
            {
                'testrule': typo.rl_testrule,
                'newrule':  typo.rl_testrule
            },
            typo.Typography('testrule', {'newrule': 'testrule'}).rules
        )
        self.assertEqual(
            ['testrule', 'newrule'],
            typo.Typography('testrule', {'newrule': 'testrule'}).rules_names
        )

    def testExpandSimpleCallableArgs(self):
        self.assertEqual(
            {'cb_testrule': cb_testrule},
            typo.Typography(cb_testrule).rules
        )
        self.assertEqual(
            ['cb_testrule'],
            typo.Typography(cb_testrule).rules_names
        )
    
    def testExpandDictCallableArgs(self):
        self.assertEqual(
            {
                'cb_testrule': cb_testrule,
                'newrule': cb_testrule
            },
            typo.Typography(cb_testrule, {'newrule': cb_testrule}).rules
        )
        self.assertEqual(
            ['cb_testrule', 'newrule'],
            typo.Typography(cb_testrule, {'newrule': cb_testrule}).rules_names
        )

    def testExpandMixedArgs(self):
        self.assertEqual(
            {
                'cb_testrule': cb_testrule,
                'newrule': typo.rl_testrule
            },
            typo.Typography(cb_testrule, newrule='testrule').rules
        )
        self.assertEqual(
            ['cb_testrule', 'newrule'],
            typo.Typography(cb_testrule, newrule='testrule').rules_names
        )
        self.assertEqual(
            {
                'cb_testrule': cb_testrule,
                'testrule': typo.rl_testrule
            },
            typo.Typography(cb_testrule, 'testrule').rules
        )
        self.assertEqual(
            ['cb_testrule', 'testrule'],
            typo.Typography(cb_testrule, 'testrule').rules_names
        )

    def testRecommendedArgsStyle(self):
        lambdarule = lambda x: x
        self.assertEqual(
            {
                'cb_testrule': cb_testrule,
                'testrule': typo.rl_testrule,
                'newrule': lambdarule
            },
            typo.Typography([cb_testrule], ['testrule'], {'newrule': lambdarule}).rules
        )
        self.assertEqual(
            ['cb_testrule', 'testrule', 'newrule'],
            typo.Typography([cb_testrule], ['testrule'], {'newrule': lambdarule}).rules_names
        )


class RulesTestCase(unittest.TestCase):

    def checkRule(self, name, input_value, expected_result):
        """
        Check how rule is acted on input_value with expected_result
        """
        self.assertEqual(
            expected_result,
            typo._get_rule_by_name(name)(input_value)
        )
    
    def testCleanspaces(self):
        """
        Unit-test for cleanspaces rule
        """
        self.checkRule(
            'cleanspaces',
            " Точка ,точка , запятая, вышла рожица  кривая . ",
            "Точка, точка, запятая, вышла рожица кривая."
        )
        self.checkRule(
            'cleanspaces',
            " Точка ,точка , %(n)sзапятая,%(n)s вышла рожица  кривая . " % {'n': os.linesep},
            "Точка, точка,%(n)sзапятая,%(n)sвышла рожица кривая." % {'n': os.linesep}
        )
        self.checkRule(
            'cleanspaces',
            "Газета ( ее принес мальчишка утром ) всё еще лежала на столе.",
            "Газета (ее принес мальчишка утром) всё еще лежала на столе.",
        )
        self.checkRule(
            'cleanspaces',
            "Газета, утром принесенная мальчишкой ( это был сосед, подзарабатывающий летом ) , всё еще лежала на столе.",
            "Газета, утром принесенная мальчишкой (это был сосед, подзарабатывающий летом), всё еще лежала на столе.",
        )
        self.checkRule(
            'cleanspaces',
            "Что это?!?!",
            "Что это?!?!",
        )

    def testEllipsis(self):
        """
        Unit-test for ellipsis rule
        """
        self.checkRule(
            'ellipsis',
            "Быть или не быть, вот в чем вопрос...%(n)s%(n)sШекспир" % {'n': os.linesep},
            "Быть или не быть, вот в чем вопрос…%(n)s%(n)sШекспир" % {'n': os.linesep}
        )
        self.checkRule(
            'ellipsis',
            "Мдя..... могло быть лучше",
            "Мдя..... могло быть лучше"
        )
        self.checkRule(
            'ellipsis',
            "...Дааааа",
            "…Дааааа"
        )
        self.checkRule(
            'ellipsis',
            "... Дааааа",
            "…Дааааа"
        )

    def testInitials(self):
        """
        Unit-test for initials rule
        """
        self.checkRule(
            'initials',
            'Председатель В.И.Иванов выступил на собрании',
            'Председатель В.И.\u2009Иванов выступил на собрании',
        )
        self.checkRule(
            'initials',
            'Председатель В.И. Иванов выступил на собрании',
            'Председатель В.И.\u2009Иванов выступил на собрании',
        )
        self.checkRule(
            'initials',
            '1. В.И.Иванов%(n)s2. С.П.Васечкин'% {'n': os.linesep},
            '1. В.И.\u2009Иванов%(n)s2. С.П.\u2009Васечкин' % {'n': os.linesep}
        )
        self.checkRule(
            'initials',
            'Комиссия в составе директора В.И.Иванова и главного бухгалтера С.П.Васечкина постановила',
            'Комиссия в составе директора В.И.\u2009Иванова и главного бухгалтера С.П.\u2009Васечкина постановила'
        )

    def testDashes(self):
        """
        Unit-test for dashes rule
        """
        self.checkRule(
            'dashes',
            '- Я пошел домой... - Может останешься? - Нет, ухожу.',
            '\u2014 Я пошел домой... \u2014 Может останешься? \u2014 Нет, ухожу.'
        )
        self.checkRule(
            'dashes',
            '-- Я пошел домой... -- Может останешься? -- Нет, ухожу.',
            '\u2014 Я пошел домой... \u2014 Может останешься? \u2014 Нет, ухожу.'
        )
        self.checkRule(
            'dashes',
            '-- Я\u202fпошел домой…\u202f-- Может останешься?\u202f-- Нет,\u202fухожу.',
            '\u2014 Я\u202fпошел домой…\u202f\u2014 Может останешься?\u202f\u2014 Нет,\u202fухожу.'
        )
        self.checkRule(
            'dashes',
            'Ползать по-пластунски',
            'Ползать по-пластунски',
        )
        self.checkRule(
            'dashes',
            'Диапазон: 9-15',
            'Диапазон: 9\u201315',
        )

    def testWordglue(self):
        """
        Unit-test for wordglue rule
        """
        self.checkRule(
            'wordglue',
            'Вроде бы он согласен',
            'Вроде\u202fбы\u202fон\u202fсогласен',
        )
        self.checkRule(
            'wordglue',
            'Он не поверил своим глазам',
            'Он\u202fне\u202fповерил своим\u202fглазам',
        )
        self.checkRule(
            'wordglue',
            'Это - великий и ужасный Гудвин',
            'Это\u202f- великий и\u202fужасный\u202fГудвин',
        )
        self.checkRule(
            'wordglue',
            'Это \u2014 великий и ужасный Гудвин',
            'Это\u202f\u2014 великий и\u202fужасный\u202fГудвин',
        )
        self.checkRule(
            'wordglue',
            '-- Я пошел домой… -- Может останешься? -- Нет, ухожу.',
            '-- Я\u202fпошел домой…\u202f-- Может останешься?\u202f-- Нет,\u202fухожу.'
        )
        self.checkRule(
            'wordglue',
            'увидел в газете (это была "Сермяжная правда" № 45) рубрику Weather Forecast',
            'увидел в\u202fгазете (это\u202fбыла "Сермяжная правда" № 45) рубрику Weather\u202fForecast',
        )

    def testMarks(self):
        """
        Unit-test for marks rule
        """
        self.checkRule(
            'marks',
            "Когда В. И. Пупкин увидел в газете рубрику Weather Forecast(r), он не поверил своим глазам \u2014 температуру обещали +-451F.",
            "Когда В. И. Пупкин увидел в газете рубрику Weather Forecast®, он не поверил своим глазам \u2014 температуру обещали ±451\u202f°F."
        )
        self.checkRule(
            'marks',
            "14 Foo",
            "14 Foo"
        )
        self.checkRule(
            'marks',
            "Coca-cola(tm)",
            "Coca-cola™"
        )
        self.checkRule(
            'marks',
            '(c) 2008 Юрий Юревич',
            '©\u202f2008 Юрий Юревич'
        )
        self.checkRule(
            'marks',
            "Microsoft (R) Windows (tm)",
            "Microsoft® Windows™"
        )
        self.checkRule(
            'marks',
            "Школа-гимназия No 3",
            "Школа-гимназия №\u20093",
        )
        self.checkRule(
            'marks',
            "Школа-гимназия No3",
            "Школа-гимназия №\u20093",
        )
        self.checkRule(
            'marks',
            "Школа-гимназия №3",
            "Школа-гимназия №\u20093",
        )

    def testQuotes(self):
        """
        Unit-test for quotes rule
        """
        self.checkRule(
            'quotes',
            "ООО \"МСК \"Аско-Забота\"",
            "ООО «МСК «Аско-Забота»"
        )
        self.checkRule(
            'quotes',
            "ООО\u202f\"МСК\u202f\"Аско-Забота\"",
            "ООО\u202f«МСК\u202f«Аско-Забота»"
        )
        self.checkRule(
            'quotes',
            "Двигатели 'Pratt&Whitney'",
            "Двигатели “Pratt&Whitney”"
        )
        self.checkRule(
            'quotes',
            "\"Вложенные \"кавычки\" - бич всех типографик\", не правда ли",
            "«Вложенные «кавычки» - бич всех типографик», не правда ли",
        )
        self.checkRule(
            'quotes',
            "Двигатели 'Pratt&Whitney' никогда не использовались на самолетах \"Аэрофлота\"",
            "Двигатели “Pratt&Whitney” никогда не использовались на самолетах «Аэрофлота»"
        )


class TypographyTestCase(unittest.TestCase):
    """
    Tests for pytils.typo.typography
    """
    def checkTypo(self, input_value, expected_value):
        """
        Helper for checking typo.typography
        """
        self.assertEqual(expected_value, typo.typography(input_value))
    
    def testPupkin(self):
        """
        Unit-test on pupkin-text
        """
        self.checkTypo(
        """...Когда В. И. Пупкин увидел в газете ( это была "Сермяжная правда" № 45) рубрику Weather Forecast(r), он не поверил своим глазам - температуру обещали +-451F.""",
        """…Когда В.И.\u2009Пупкин увидел в\u202fгазете (это\u202fбыла «Сермяжная правда» №\u200945) рубрику Weather Forecast®, он\u202fне\u202fповерил своим глазам\u202f\u2014 температуру обещали ±451\u202f°F.""")


if __name__ == '__main__':
    unittest.main()

