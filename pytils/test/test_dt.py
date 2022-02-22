# -*- coding: utf-8 -*-
"""
Unit-tests for pytils.dt
"""

import datetime
import time
import unittest

import pytils


class DistanceOfTimeInWordsTestCase(unittest.TestCase):
    """
    Test case for pytils.dt.distance_of_time_in_words
    """

    def setUp(self):
        """
        Setting up environment for tests
        """
        self.time = 1156862275.7711999
        self.dtime = {}
        self.updateTime(self.time)

    def updateTime(self, _time):
        """Update all time-related values for current time """
        self.dtime['10sec_ago'] = _time - 10
        self.dtime['1min_ago'] = _time - 60
        self.dtime['10min_ago'] = _time - 600
        self.dtime['59min_ago'] = _time - 3540
        self.dtime['59min59sec_ago'] = _time - 3599
        self.dtime['1hr_ago'] = _time - 3600
        self.dtime['1hr1sec_ago'] = _time - 3601
        self.dtime['1hr59sec_ago'] = _time - 3659
        self.dtime['1hr1min_ago'] = _time - 3660
        self.dtime['1hr2min_ago'] = _time - 3720
        self.dtime['10hr_ago'] = _time - 36600
        self.dtime['1day_ago'] = _time - 87600
        self.dtime['1day1hr_ago'] = _time - 90600
        self.dtime['2day_ago'] = _time - 87600*2
        self.dtime['4day1min_ago'] = _time - 87600*4 - 60

        self.dtime['in_10sec'] = _time + 10
        self.dtime['in_1min'] = _time + 61
        self.dtime['in_10min'] = _time + 601
        self.dtime['in_1hr'] = _time + 3721
        self.dtime['in_10hr'] = _time + 36601
        self.dtime['in_1day'] = _time + 87601
        self.dtime['in_1day1hr'] = _time + 90601
        self.dtime['in_2day'] = _time + 87600*2 + 1

    def ckDefaultAccuracy(self, typ, estimated):
        """
        Checks with default value for accuracy
        """
        t0 = time.time()
        # --- change state !!! attention
        self.updateTime(t0)
        # ---
        t1 = self.dtime[typ]
        res = pytils.dt.distance_of_time_in_words(from_time=t1, to_time=t0)
        # --- revert state to original value
        self.updateTime(self.time)
        # ---
        self.assertEqual(res, estimated)

    def ckDefaultTimeAndAccuracy(self, typ, estimated):
        """
        Checks with default accuracy and default time
        """
        t0 = time.time()
        # --- change state !!! attention
        self.updateTime(t0)
        # ---
        t1 = self.dtime[typ]
        res = pytils.dt.distance_of_time_in_words(t1)
        # --- revert state to original value
        self.updateTime(self.time)
        # ---
        self.assertEqual(res, estimated)

    def ckDefaultToTime(self, typ, accuracy, estimated):
        """
        Checks with default value of time
        """
        t0 = time.time()
        # --- change state !!! attention
        self.updateTime(t0)
        # ---
        t1 = self.dtime[typ]
        res = pytils.dt.distance_of_time_in_words(t1, accuracy)
        # --- revert state to original value
        self.updateTime(self.time)
        # ---
        self.assertEqual(res, estimated)

    def testDOTIWDefaultAccuracy(self):
        """
        Unit-test for distance_of_time_in_words with default accuracy
        """
        self.ckDefaultAccuracy("10sec_ago", "менее минуты назад")
        self.ckDefaultAccuracy("1min_ago", "1 минуту назад")
        self.ckDefaultAccuracy("10min_ago", "10 минут назад")
        self.ckDefaultAccuracy("59min_ago", "59 минут назад")
        self.ckDefaultAccuracy("59min59sec_ago", "59 минут назад")
        self.ckDefaultAccuracy("1hr_ago", "1 час назад")
        self.ckDefaultAccuracy("1hr1sec_ago", "1 час назад")
        self.ckDefaultAccuracy("1hr59sec_ago", "1 час назад")
        self.ckDefaultAccuracy("1hr1min_ago", "1 час назад")
        self.ckDefaultAccuracy("1hr2min_ago", "1 час назад")
        self.ckDefaultAccuracy("10hr_ago", "10 часов назад")
        self.ckDefaultAccuracy("1day_ago", "1 день назад")
        self.ckDefaultAccuracy("1day1hr_ago", "1 день назад")
        self.ckDefaultAccuracy("2day_ago", "2 дня назад")

        self.ckDefaultAccuracy("in_10sec", "менее чем через минуту")
        self.ckDefaultAccuracy("in_1min", "через 1 минуту")
        self.ckDefaultAccuracy("in_10min", "через 10 минут")
        self.ckDefaultAccuracy("in_1hr", "через 1 час")
        self.ckDefaultAccuracy("in_10hr", "через 10 часов")
        self.ckDefaultAccuracy("in_1day", "через 1 день")
        self.ckDefaultAccuracy("in_1day1hr", "через 1 день")
        self.ckDefaultAccuracy("in_2day", "через 2 дня")

    def testDOTIWDefaultAccuracyDayAndMinute(self):
        """
        Unit-tests for distance_of_time_in_words with default accuracy and to_time
        """
        self.ckDefaultTimeAndAccuracy("4day1min_ago", "4 дня назад")

        self.ckDefaultTimeAndAccuracy("10sec_ago", "менее минуты назад")
        self.ckDefaultTimeAndAccuracy("1min_ago", "минуту назад")
        self.ckDefaultTimeAndAccuracy("10min_ago", "10 минут назад")
        self.ckDefaultTimeAndAccuracy("59min_ago", "59 минут назад")
        self.ckDefaultTimeAndAccuracy("59min59sec_ago", "59 минут назад")
        self.ckDefaultTimeAndAccuracy("1hr_ago", "час назад")
        self.ckDefaultTimeAndAccuracy("1hr1sec_ago", "час назад")
        self.ckDefaultTimeAndAccuracy("1hr59sec_ago", "час назад")
        self.ckDefaultTimeAndAccuracy("1hr1min_ago", "час назад")
        self.ckDefaultTimeAndAccuracy("1hr2min_ago", "час назад")
        self.ckDefaultTimeAndAccuracy("10hr_ago", "10 часов назад")
        self.ckDefaultTimeAndAccuracy("1day_ago", "вчера")
        self.ckDefaultTimeAndAccuracy("1day1hr_ago", "вчера")
        self.ckDefaultTimeAndAccuracy("2day_ago", "позавчера")

        self.ckDefaultTimeAndAccuracy("in_10sec", "менее чем через минуту")
        self.ckDefaultTimeAndAccuracy("in_1min", "через минуту")
        self.ckDefaultTimeAndAccuracy("in_10min", "через 10 минут")
        self.ckDefaultTimeAndAccuracy("in_1hr", "через час")
        self.ckDefaultTimeAndAccuracy("in_10hr", "через 10 часов")
        self.ckDefaultTimeAndAccuracy("in_1day", "завтра")
        self.ckDefaultTimeAndAccuracy("in_1day1hr", "завтра")
        self.ckDefaultTimeAndAccuracy("in_2day", "послезавтра")

    def test4Days1MinuteDaytimeBug2(self):
        from_time = datetime.datetime.now() - datetime.timedelta(days=4, minutes=1)
        res = pytils.dt.distance_of_time_in_words(from_time)
        self.assertEqual(res, "4 дня назад")

    def testDOTIWDefaultToTimeAcc1(self):
        """
        Unit-tests for distance_of_time_in_words with default to_time and accuracy=1
        """
        # accuracy = 1
        self.ckDefaultToTime("10sec_ago", 1, "менее минуты назад")
        self.ckDefaultToTime("1min_ago", 1, "минуту назад")
        self.ckDefaultToTime("10min_ago", 1,  "10 минут назад")
        self.ckDefaultToTime("59min_ago", 1, "59 минут назад")
        self.ckDefaultToTime("59min59sec_ago", 1, "59 минут назад")
        self.ckDefaultToTime("1hr_ago", 1, "час назад")
        self.ckDefaultToTime("1hr1sec_ago", 1, "час назад")
        self.ckDefaultToTime("1hr59sec_ago", 1, "час назад")
        self.ckDefaultToTime("1hr1min_ago", 1, "час назад")
        self.ckDefaultToTime("1hr2min_ago", 1, "час назад")
        self.ckDefaultToTime("10hr_ago", 1, "10 часов назад")
        self.ckDefaultToTime("1day_ago", 1, "вчера")
        self.ckDefaultToTime("1day1hr_ago", 1, "вчера")
        self.ckDefaultToTime("2day_ago", 1, "позавчера")

        self.ckDefaultToTime("in_10sec", 1, "менее чем через минуту")
        self.ckDefaultToTime("in_1min", 1, "через минуту")
        self.ckDefaultToTime("in_10min", 1, "через 10 минут")
        self.ckDefaultToTime("in_1hr", 1, "через час")
        self.ckDefaultToTime("in_10hr", 1, "через 10 часов")
        self.ckDefaultToTime("in_1day", 1, "завтра")
        self.ckDefaultToTime("in_1day1hr", 1, "завтра")
        self.ckDefaultToTime("in_2day", 1, "послезавтра")
        
    def testDOTIWDefaultToTimeAcc2(self):
        """
        Unit-tests for distance_of_time_in_words with default to_time and accuracy=2
        """
        # accuracy = 2
        self.ckDefaultToTime("10sec_ago", 2, "менее минуты назад")
        self.ckDefaultToTime("1min_ago", 2, "минуту назад")
        self.ckDefaultToTime("10min_ago", 2, "10 минут назад")
        self.ckDefaultToTime("59min_ago", 2, "59 минут назад")
        self.ckDefaultToTime("59min59sec_ago", 2, "59 минут назад")
        self.ckDefaultToTime("1hr_ago", 2, "час назад")
        self.ckDefaultToTime("1hr1sec_ago", 2, "час назад")
        self.ckDefaultToTime("1hr59sec_ago", 2, "час назад")
        self.ckDefaultToTime("1hr1min_ago", 2, "1 час 1 минуту назад")
        self.ckDefaultToTime("1hr2min_ago", 2, "1 час 2 минуты назад")
        self.ckDefaultToTime("10hr_ago", 2, "10 часов 10 минут назад")
        self.ckDefaultToTime("1day_ago", 2, "вчера")
        self.ckDefaultToTime("1day1hr_ago", 2, "1 день 1 час назад")
        self.ckDefaultToTime("2day_ago", 2, "позавчера")

        self.ckDefaultToTime("in_10sec", 2, "менее чем через минуту")
        self.ckDefaultToTime("in_1min", 2, "через минуту")
        self.ckDefaultToTime("in_10min", 2, "через 10 минут")
        self.ckDefaultToTime("in_1hr", 2, "через 1 час 2 минуты")
        self.ckDefaultToTime("in_10hr", 2, "через 10 часов 10 минут")
        self.ckDefaultToTime("in_1day", 2, "завтра")
        self.ckDefaultToTime("in_1day1hr", 2, "через 1 день 1 час")
        self.ckDefaultToTime("in_2day", 2, "послезавтра")
        
    def testDOTIWDefaultToTimeAcc3(self):
        """
        Unit-tests for distance_of_time_in_words with default to_time and accuracy=3
        """
        # accuracy = 3
        self.ckDefaultToTime("10sec_ago", 3, "менее минуты назад")
        self.ckDefaultToTime("1min_ago", 3, "минуту назад")
        self.ckDefaultToTime("10min_ago", 3, "10 минут назад")
        self.ckDefaultToTime("59min_ago", 3, "59 минут назад")
        self.ckDefaultToTime("59min59sec_ago", 3, "59 минут назад")
        self.ckDefaultToTime("1hr_ago", 3, "час назад")
        self.ckDefaultToTime("1hr1sec_ago", 3, "час назад")
        self.ckDefaultToTime("1hr59sec_ago", 3, "час назад")
        self.ckDefaultToTime("1hr1min_ago", 3, "1 час 1 минуту назад")
        self.ckDefaultToTime("1hr2min_ago", 3, "1 час 2 минуты назад")
        self.ckDefaultToTime("10hr_ago", 3, "10 часов 10 минут назад")
        self.ckDefaultToTime("1day_ago", 3, "1 день 0 часов 20 минут назад")
        self.ckDefaultToTime("1day1hr_ago", 3, "1 день 1 час 10 минут назад")
        self.ckDefaultToTime("2day_ago", 3, "2 дня 0 часов 40 минут назад")

        self.ckDefaultToTime("in_10sec", 3, "менее чем через минуту")
        self.ckDefaultToTime("in_1min", 3, "через минуту")
        self.ckDefaultToTime("in_10min", 3, "через 10 минут")
        self.ckDefaultToTime("in_1hr", 3, "через 1 час 2 минуты")
        self.ckDefaultToTime("in_10hr", 3, "через 10 часов 10 минут")
        self.ckDefaultToTime("in_1day", 3, "через 1 день 0 часов 20 минут")
        self.ckDefaultToTime("in_1day1hr", 3, "через 1 день 1 час 10 минут")
        self.ckDefaultToTime("in_2day", 3, "через 2 дня 0 часов 40 минут")

    def testDOTWDatetimeType(self):
        """
        Unit-tests for testing datetime.datetime as input values
        """
        first_time = datetime.datetime.now()
        second_time = first_time + datetime.timedelta(0, 1000)
        self.assertEqual(
            pytils.dt.distance_of_time_in_words(
                from_time=first_time,
                accuracy=1,
                to_time=second_time
            ),
            "16 минут назад"
        )

    def testDOTIWExceptions(self):
        """
        Unit-tests for testings distance_of_time_in_words' exceptions
        """
        self.assertRaises(ValueError, pytils.dt.distance_of_time_in_words, time.time(), 0)
    
    def testIssue25DaysFixed(self):
        """
        Unit-test for testing that Issue#25 is fixed (err when accuracy==1, days<>0, hours==1)
        """
        d_days = datetime.datetime.now() - datetime.timedelta(13, 3620)
        self.assertEqual(
            pytils.dt.distance_of_time_in_words(d_days),
            "13 дней назад"
        )

    def testIssue25HoursFixed(self):
        """
        Unit-test for testing that Issue#25 is fixed (err when accuracy==1, hours<>0, minutes==1)
        """
        d_hours = datetime.datetime.now() - datetime.timedelta(0, 46865)
        self.assertEqual(
            pytils.dt.distance_of_time_in_words(d_hours),
            "13 часов назад"
        )
        

class RuStrftimeTestCase(unittest.TestCase):
    """
    Test case for pytils.dt.ru_strftime
    """

    def setUp(self):
        """
        Setting up environment for tests
        """
        self.date = datetime.date(2006, 8, 25)
    
    def ck(self, format, estimates, date=None):
        """
        Checks w/o inflected
        """
        if date is None:
            date = self.date
        res = pytils.dt.ru_strftime(format, date)
        self.assertEqual(res, estimates)

    def ckInflected(self, format, estimates, date=None):
        """
        Checks with inflected
        """
        if date is None:
            date = self.date
        res = pytils.dt.ru_strftime(format, date, True)
        self.assertEqual(res, estimates)

    def ckInflectedDay(self, format, estimates, date=None):
        """
        Checks with inflected day
        """
        if date is None:
            date = self.date
        res = pytils.dt.ru_strftime(format, date, inflected_day=True)
        self.assertEqual(res, estimates)

    def ckPreposition(self, format, estimates, date=None):
        """
        Checks with inflected day
        """
        if date is None:
            date = self.date
        res = pytils.dt.ru_strftime(format, date, preposition=True)
        self.assertEqual(res, estimates)

    def testRuStrftime(self):
        """
        Unit-tests for pytils.dt.ru_strftime
        """
        self.ck("тест %a", "тест пт")
        self.ck("тест %A", "тест пятница")
        self.ck("тест %b", "тест авг")
        self.ck("тест %B", "тест август")
        self.ckInflected("тест %B", "тест августа")
        self.ckInflected("тест выполнен %d %B %Y года", "тест выполнен 25 августа 2006 года")
        self.ckInflectedDay("тест выполнен в %A", "тест выполнен в пятницу")
    
    def testRuStrftimeWithPreposition(self):
        """
        Unit-tests for pytils.dt.ru_strftime with preposition option
        """
        self.ckPreposition("тест %a", "тест в\xa0пт")
        self.ckPreposition("тест %A", "тест в\xa0пятницу")
        self.ckPreposition("тест %A", "тест во\xa0вторник", datetime.date(2007, 6, 5))
    
    def testRuStrftimeZeros(self):
        """
        Unit-test for testing that Issue#24 is correctly implemented
        
        It means, 1 April 2007, but 01.04.2007
        """
        self.ck("%d.%m.%Y", "01.04.2007", datetime.date(2007, 4, 1))
        self.ckInflected("%d %B %Y", "1 апреля 2007", datetime.date(2007, 4, 1))

    def testIssue20Fixed(self):
        """
        Unit-test for testing that Issue#20 is fixed (typo)
        """
        self.assertEqual(
            "воскресенье",
            pytils.dt.ru_strftime(
                "%A",
                datetime.date(2007, 3, 18),
                inflected_day=True
            )
         )

    def test_special_case(self):
        self.assertEqual(
            "октябрь",
            pytils.dt.ru_strftime(
                '%B',
                inflected=False,
                date=datetime.datetime.fromtimestamp(1540209256)
            ),
        )


if __name__ == '__main__':
    unittest.main()
