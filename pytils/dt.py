# -*- coding: utf-8 -*-
# -*- test-case-name: pytils.test.test_dt -*-
# PyTils - simple processing for russian strings
# Copyright (C) 2006-2007  Yury Yurevich
#
# http://gorod-omsk.ru/blog/pythy/projects/pytils/
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
Russian dates without locales
"""

__id__ = __revision__ = "$Id$"
__url__ = "$URL$"

import datetime

from pytils import numeral, utils

DAY_ALTERNATIVES = {
    1: (u"вчера", u"завтра"),
    2: (u"позавчера", u"послезавтра")
    }  #: Day alternatives (i.e. one day ago -> yesterday)

DAY_VARIANTS = (
    u"день",
    u"дня",
    u"дней",
    )  #: Forms (1, 2, 5) for noun 'day'

HOUR_VARIANTS = (
    u"час",
    u"часа",
    u"часов",
    )  #: Forms (1, 2, 5) for noun 'hour'

MINUTE_VARIANTS = (
    u"минуту",
    u"минуты",
    u"минут",
    )  #: Forms (1, 2, 5) for noun 'minute'

PREFIX_IN = u"через"  #: Prefix 'in' (i.e. B{in} three hours)
SUFFIX_AGO = u"назад"  #: Prefix 'ago' (i.e. three hours B{ago})

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
    )  #: Month names (abbreviated, full, inflected)

DAY_NAMES = (
    (u"пн", u"понедельник", u"понедельник"),
    (u"вт", u"вторник", u"вторник"),
    (u"ср", u"среда", u"среду"),
    (u"чт", u"четверг", u"четверг"),
    (u"пт", u"пятница", u"пятницу"),
    (u"сб", u"суббота", u"субботу"),
    (u"вск", u"воскресенье", u"субботу"),
    )  #: Day names (abbreviated, full, inflected)


def distance_of_time_in_words(from_time, accuracy=1, to_time=None):
    """
    Represents distance of time in words

    @param from_time: source time (in seconds from epoch)
    @type from_time: C{int}, C{float} or C{datetime.datetime}

    @param accuracy: level of accuracy (1..3), default=1
    @type accuracy: C{int}

    @param to_time: target time (in seconds from epoch),
        default=None translates to current time
    @type to_time: C{int}, C{float} or C{datetime.datetime}

    @return: distance of time in words
    @rtype: unicode

    @raise TypeError: input parameters' check failed
    @raise ValueError: accuracy is lesser or equal zero
    """
    current = False

    if to_time is None:
        current = True
        to_time = datetime.datetime.now()

    utils.check_type('from_time', (int, float, datetime.datetime))
    utils.check_type('to_time', (int, float, datetime.datetime))
    utils.check_type('accuracy', int)
    utils.check_positive('accuracy', strict=True)

    if not isinstance(from_time, datetime.datetime):
        from_time = datetime.datetime.fromtimestamp(from_time)

    if not isinstance(to_time, datetime.datetime):
        to_time = datetime.datetime.fromtimestamp(to_time)

    dt_delta = to_time - from_time
    difference = dt_delta.days*86400 + dt_delta.seconds

    seconds_orig = int(abs(difference))
    minutes_orig = int(abs(difference)/60.0)
    hours_orig = int(abs(difference)/3600.0)
    days_orig = int(abs(difference)/86400.0)
    in_future = from_time > to_time

    words = []
    values = []
    alternatives = []

    days = days_orig
    hours = hours_orig - days_orig*24

    words.append(u"%d %s" % (days, numeral.choose_plural(days, DAY_VARIANTS)))
    values.append(days)

    words.append(u"%d %s" % \
                  (hours, numeral.choose_plural(hours, HOUR_VARIANTS)))
    values.append(hours)

    hours == 1 and current and alternatives.append(u"час")

    minutes = minutes_orig - hours_orig*60

    words.append(u"%d %s" % (minutes,
                              numeral.choose_plural(minutes, MINUTE_VARIANTS)))
    values.append(minutes)

    minutes == 1 and current and alternatives.append(u"минуту")

    real_words = words
    # убираем из values и words конечные нули
    while values and not values[-1]:
        values.pop()
        words.pop()
    # убираем из values и words начальные нули
    while values and not values[0]:
        values.pop(0)
        words.pop(0)
    limit = min(accuracy, len(words))
    real_words = words[:limit]
    real_values = values[:limit]
    # снова убираем конечные нули
    while real_values and not real_values[-1]:
        real_values.pop()
        real_words.pop()
        limit -= 1

    real_str = u" ".join(real_words)

    # альтернативные варианты нужны только если в real_words одно значение
    # и, вдобавок, если используется текущее время
    alter_str = limit == 1 and current and \
                alternatives and alternatives[0]
    _result_str = alter_str or real_str
    result_str = in_future and u"%s %s" % (PREFIX_IN, _result_str) \
                           or u"%s %s" % (_result_str, SUFFIX_AGO)

    # если же прошло менее минуты, то real_words -- пустой, и поэтому
    # нужно брать alternatives[0], а не result_str
    zero_str = minutes == 0 and not real_words and \
            (in_future and u"менее чем через минуту" \
                        or u"менее минуты назад")

    # нужно использовать вчера/позавчера/завтра/послезавтра
    # если days 1..2 и в real_words одно значение
    day_alternatives = DAY_ALTERNATIVES.get(days, False)
    alternate_day = day_alternatives and current and limit == 1 and \
                    ((in_future and day_alternatives[1]) \
                                 or day_alternatives[0])

    final_str = not real_words and zero_str or alternate_day or result_str

    return final_str


def ru_strftime(format=u"%d.%m.%Y", date=None, inflected=False, inflected_day=False):
    """
    Russian strftime without locale

    @param format: strftime format, default=u'%d.%m.%Y'
    @type format: C{unicode}

    @param date: date value, default=None translates to today
    @type date: C{datetime.date} or C{datetime.datetime}

    @return: strftime string
    @rtype: unicode

    @raise TypeError: input parameters' check failed
    """
    if date is None:
        date = datetime.datetime.today()
    utils.check_type('date', (datetime.date, datetime.datetime))
    utils.check_type('format', unicode)

    midx = inflected and 2 or 1
    didx = inflected_day and 2 or 1

    format = format.replace(u'%a', DAY_NAMES[date.weekday()][0])
    format = format.replace(u'%A', DAY_NAMES[date.weekday()][didx])
    format = format.replace(u'%b', MONTH_NAMES[date.month-1][0])
    format = format.replace(u'%B', MONTH_NAMES[date.month-1][midx])

    # strftime must be str, so encode it to utf8:
    s_format = format.encode("utf-8")
    s_res = date.strftime(s_format)
    # and back to unicode
    u_res = s_res.decode("utf-8")

    return u_res
