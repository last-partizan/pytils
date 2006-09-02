# -*- coding: utf-8 -*-
# -*- test-case-name: pytils.test.test_dt -*-
# License: GNU GPL2
# Author: Pythy <the.pythy@gmail.com>
"""
Russian dates without locales
"""

__id__ = "$Id$"
__url__ = "$URL$"

import time
import datetime

from pytils import numeral

TOMORROW = u"завтра"
YESTERDAY = u"вчера"
THE_DAY_AFTER_TOMORROW = u"послезавтра"
THE_DAY_BEFORE_YESTERDAY = u"позавчера"
DAY_VARIANTS = (
    u"день",
    u"дня",
    u"дней",
    )
HOUR_VARIANTS = (
    u"час",
    u"часа",
    u"часов",
    )
MINUTE_VARIANTS = (
    u"минуту",
    u"минуты",
    u"минут",
    )
PREFIX_IN = u"через"
SUFFIX_AGO = u"назад"

MONTH_NAMES = (
    (u"янв", u"январь", u"января"),
    (u"фев", u"февраль", u"февраля"),
    (u"мар", u"март", u"марта"),
    (u"апр", u"апрель", u"апреля"),
    (u"май", u"май", u"мая"),
    (u"июн", u"июнь", u"июня"),
    (u"июл", u"июль", u"июля"),
    (u"авг", u"август", u"августа"),
    (u"сен", u"сентябрь", u"сентября"),
    (u"окт", u"октябрь", u"октября"),
    (u"ноя", u"ноябрь", u"ноября"),
    (u"дек", u"декабрь", u"декабря"),
    )

DAY_NAMES = (
    (u"пн", u"понедельник"),
    (u"вт", u"вторник"),
    (u"ср", u"среда"),
    (u"чт", u"четверг"),
    (u"пт", u"пятница"),
    (u"сб", u"суббота"),
    (u"вск", u"воскресенье"),
    )


def distance_of_time_in_words(from_time, accuracy=1, to_time=None):
    """
    Represents distance of time in words

    @param from_time: source time (in seconds from epoch)
    @type from_time: C{int} or C{float}
    @param accuracy: level of accuracy (1..3), default=1
    @type accuracy: C{int}
    @param to_time: target time (in seconds from epoch), default=None translates to current time
    @type to_time: C{int} or C{float}

    @return: distance of time in words
    @rtype: unicode

    @raise AssertionError: input parameters' check failed
    """
    current = False
    
    if to_time is None:
        current = True
        to_time = time.time()

    assert isinstance(from_time, (int, float))
    assert isinstance(to_time, (int, float))
    assert isinstance(accuracy, int) and accuracy > 0

    seconds = int(abs(to_time - from_time))
    minutes = int(abs(to_time - from_time)/60.0)
    hours   = int(abs(to_time - from_time)/3600.0)
    days =    int(abs(to_time - from_time)/86400.0)
    in_future = from_time > to_time

    st = []
    st_val = []
    st_alt = []

    hours_orig = hours
    hours = hours - days*24

    if days > 0:
        st.append(u"%d %s" % (days, numeral.choose_plural(days, DAY_VARIANTS)))
        st_val.append(days)

        if days == 1:
            if in_future:
                st_alt.append(TOMORROW)
            else:
                st_alt.append(YESTERDAY)
        elif days == 2:
            if in_future:
                st_alt.append(THE_DAY_AFTER_TOMORROW)
            else:
                st_alt.append(THE_DAY_BEFORE_YESTERDAY)
        
    if hours > 0 or (hours == 0 and days > 0):
        st.append(u"%d %s" % (hours, numeral.choose_plural(hours, HOUR_VARIANTS)))
        st_val.append(hours)

    if hours == 1:
        st_alt.append(u"час")

    minutes = minutes - hours_orig*60

    if minutes > 0 or (minutes == 0 and hours > 0):
        st.append(u"%d %s" % (minutes, numeral.choose_plural(minutes, MINUTE_VARIANTS)))
        st_val.append(minutes)

    if minutes == 1:
        st_alt.append(u"минуту")

    if minutes == 0 and not st_alt:
        if in_future:
             return u"менее чем через минуту"
        else:
            return u"менее минуты назад"

    idx = min(accuracy, len(st))
    if st_val[idx-1] == 0:
        # для того, чтобы не было 1 день 0 часов назад и т.д.
        idx -= 1

    if idx == 1 and st_alt and current:
        if in_future:
            if not days:
                return u"%s %s" % (PREFIX_IN, st_alt[0])
            else:
                return st_alt[0]
        else:
            if not days:
                return u"%s %s" % (st_alt[0], SUFFIX_AGO)
            else:
                return st_alt[0]
    
    st_str = u" ".join(filter(lambda x: len(x) > 0, st[:idx]))

    if in_future:
        return u"%s %s" % (PREFIX_IN, st_str)
    else:
        return u"%s %s" % (st_str, SUFFIX_AGO)

def ru_strftime(format=u"%d.%m.%Y", dt=None, inflected=False):
    """
    Russian strftime without locale

    @param format: strftime format, default=u'%d.%m.%Y'
    @type format: C{unicode}
    @param dt: date value, default=None translates to today
    @type dt: C{datetime.date} or C{datetime.datetime}

    @return: strftime string
    @rtype: unicode

    @raise AssertionError: input parameters' check failed
    """
    if dt is None:
        dt = datetime.datetime.today()
    assert isinstance(dt, (datetime.date, datetime.datetime))
    assert isinstance(format, unicode)
    
    if inflected:
        midx = 2
    else:
        midx = 1

    format = format.replace(u'%a', DAY_NAMES[dt.weekday()][0])
    format = format.replace(u'%A', DAY_NAMES[dt.weekday()][1])
    format = format.replace(u'%b', MONTH_NAMES[dt.month-1][0])
    format = format.replace(u'%B', MONTH_NAMES[dt.month-1][midx])

    # strftime must be str, so encode it to utf8:
    s_format = format.encode("utf-8")
    s_res = dt.strftime(s_format)
    # and back to unicode
    u_res = s_res.decode("utf-8")

    return u_res
    
