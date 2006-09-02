# -*- coding: utf-8 -*-
# License: GNU GPL2
# Author: Pythy <the.pythy@gmail.com>

__id__ = "$Id$"
__url__ = "$URL$"

import datetime
import time
import unittest

import pytils 

class DistanceOfTimeInWordsTestCase(unittest.TestCase):

    def setUp(self):
        self.t = 1156862275.7711999
        self.updateTime(self.t)

    def updateTime(self, t):
        self.t_10sec_ago = t - 10
        self.t_1min_ago = t - 60
        self.t_10min_ago = t - 600
        self.t_1hr_ago = t - 3720
        self.t_10hr_ago = t - 36600
        self.t_1day_ago = t - 87600
        self.t_1day1hr_ago = t - 90600
        self.t_2day_ago = t - 87600*2

        self.t_in_10sec = t + 10
        self.t_in_1min = t + 61
        self.t_in_10min = t + 601
        self.t_in_1hr = t + 3721
        self.t_in_10hr = t + 36601
        self.t_in_1day = t + 87601
        self.t_in_1day1hr = t + 90601
        self.t_in_2day = t + 87600*2 + 1

    def ck_default_accuracy(self, typ, estimated):
        t0 = time.time()
        # --- change state !!! attention
        self.updateTime(t0)
        # ---
        t1 = getattr(self, typ)
        res = pytils.dt.distance_of_time_in_words(from_time=t1, to_time=t0)
        # --- revert state to original value
        self.updateTime(self.t)
        # ---
        self.assertEquals(res, estimated)

    def ck_default_to_time(self, typ, accuracy, estimated):
        t0 = time.time()
        # --- change state !!! attention
        self.updateTime(t0)
        # ---
        t1 = getattr(self, typ)
        res = pytils.dt.distance_of_time_in_words(t1, accuracy)
        # --- revert state to original value
        self.updateTime(self.t)
        # ---
        self.assertEquals(res, estimated)


    def test_distance_of_time_in_words_default_accuracy(self):
        self.ck_default_accuracy("t_10sec_ago", u"менее минуты назад")
        self.ck_default_accuracy("t_1min_ago", u"1 минуту назад")
        self.ck_default_accuracy("t_10min_ago", u"10 минут назад")
        self.ck_default_accuracy("t_1hr_ago", u"1 час назад")
        self.ck_default_accuracy("t_10hr_ago", u"10 часов назад")
        self.ck_default_accuracy("t_1day_ago", u"1 день назад")
        self.ck_default_accuracy("t_1day1hr_ago", u"1 день назад")
        self.ck_default_accuracy("t_2day_ago", u"2 дня назад")

        self.ck_default_accuracy("t_in_10sec", u"менее чем через минуту")
        self.ck_default_accuracy("t_in_1min", u"через 1 минуту")
        self.ck_default_accuracy("t_in_10min", u"через 10 минут")
        self.ck_default_accuracy("t_in_1hr", u"через 1 час")
        self.ck_default_accuracy("t_in_10hr", u"через 10 часов")
        self.ck_default_accuracy("t_in_1day", u"через 1 день")
        self.ck_default_accuracy("t_in_1day1hr", u"через 1 день")
        self.ck_default_accuracy("t_in_2day", u"через 2 дня")

    def test_distance_of_time_in_words_default_to_time_acc1(self):
        # accuracy = 1
        self.ck_default_to_time("t_10sec_ago", 1, u"менее минуты назад")
        self.ck_default_to_time("t_1min_ago", 1, u"минуту назад")
        self.ck_default_to_time("t_10min_ago", 1,  u"10 минут назад")
        self.ck_default_to_time("t_1hr_ago", 1, u"час назад")
        self.ck_default_to_time("t_10hr_ago", 1, u"10 часов назад")
        self.ck_default_to_time("t_1day_ago", 1, u"вчера")
        self.ck_default_to_time("t_1day1hr_ago", 1, u"вчера")
        self.ck_default_to_time("t_2day_ago", 1, u"позавчера")

        self.ck_default_to_time("t_in_10sec", 1, u"менее чем через минуту")
        self.ck_default_to_time("t_in_1min", 1, u"через минуту")
        self.ck_default_to_time("t_in_10min", 1, u"через 10 минут")
        self.ck_default_to_time("t_in_1hr", 1, u"через час")
        self.ck_default_to_time("t_in_10hr", 1, u"через 10 часов")
        self.ck_default_to_time("t_in_1day", 1, u"завтра")
        self.ck_default_to_time("t_in_1day1hr", 1, u"завтра")
        self.ck_default_to_time("t_in_2day", 1, u"послезавтра")
        
    def test_distance_of_time_in_words_default_to_time_acc2(self):
        # accuracy = 2
        self.ck_default_to_time("t_10sec_ago", 2, u"менее минуты назад")
        self.ck_default_to_time("t_1min_ago", 2, u"минуту назад")
        self.ck_default_to_time("t_10min_ago", 2,  u"10 минут назад")
        self.ck_default_to_time("t_1hr_ago", 2, u"1 час 2 минуты назад")
        self.ck_default_to_time("t_10hr_ago", 2, u"10 часов 10 минут назад")
        self.ck_default_to_time("t_1day_ago", 2, u"вчера")
        self.ck_default_to_time("t_1day1hr_ago", 2, u"1 день 1 час назад")
        self.ck_default_to_time("t_2day_ago", 2, u"позавчера")

        self.ck_default_to_time("t_in_10sec", 2, u"менее чем через минуту")
        self.ck_default_to_time("t_in_1min", 2, u"через минуту")
        self.ck_default_to_time("t_in_10min", 2, u"через 10 минут")
        self.ck_default_to_time("t_in_1hr", 2, u"через 1 час 2 минуты")
        self.ck_default_to_time("t_in_10hr", 2, u"через 10 часов 10 минут")
        self.ck_default_to_time("t_in_1day", 2, u"завтра")
        self.ck_default_to_time("t_in_1day1hr", 2, u"через 1 день 1 час")
        self.ck_default_to_time("t_in_2day", 2, u"послезавтра")
        
    def test_distance_of_time_in_words_default_to_time_acc3(self):
        # accuracy = 3
        self.ck_default_to_time("t_10sec_ago", 3, u"менее минуты назад")
        self.ck_default_to_time("t_1min_ago", 3, u"минуту назад")
        self.ck_default_to_time("t_10min_ago", 3,  u"10 минут назад")
        self.ck_default_to_time("t_1hr_ago", 3, u"1 час 2 минуты назад")
        self.ck_default_to_time("t_10hr_ago", 3, u"10 часов 10 минут назад")
        self.ck_default_to_time("t_1day_ago", 3, u"1 день 0 часов 20 минут назад")
        self.ck_default_to_time("t_1day1hr_ago", 3, u"1 день 1 час 10 минут назад")
        self.ck_default_to_time("t_2day_ago", 3, u"2 дня 0 часов 40 минут назад")

        self.ck_default_to_time("t_in_10sec", 3, u"менее чем через минуту")
        self.ck_default_to_time("t_in_1min", 3, u"через минуту")
        self.ck_default_to_time("t_in_10min", 3, u"через 10 минут")
        self.ck_default_to_time("t_in_1hr", 3, u"через 1 час 2 минуты")
        self.ck_default_to_time("t_in_10hr", 3, u"через 10 часов 10 минут")
        self.ck_default_to_time("t_in_1day", 3, u"через 1 день 0 часов 20 минут")
        self.ck_default_to_time("t_in_1day1hr", 3, u"через 1 день 1 час 10 минут")
        self.ck_default_to_time("t_in_2day", 3, u"через 2 дня 0 часов 40 минут")

class RuStrftimeTestCase(unittest.TestCase):

    def setUp(self):
        self.d = datetime.date(2006, 8, 25)
    
    def ck(self, format, estimates):
        res = pytils.dt.ru_strftime(format, self.d)
        self.assertEquals(res, estimates)

    def ck_inflected(self, format, estimates):
        res = pytils.dt.ru_strftime(format, self.d, True)
        self.assertEquals(res, estimates)

    def test_ru_strftime(self):
        self.ck(u"тест %a", u"тест пт")
        self.ck(u"тест %A", u"тест пятница")
        self.ck(u"тест %b", u"тест авг")
        self.ck(u"тест %B", u"тест август")
        self.ck_inflected(u"тест %B", u"тест августа")
        self.ck_inflected(u"тест выполнен %d %B %Y года", u"тест выполнен 25 августа 2006 года")

if __name__ == '__main__':
    unittest.main()
