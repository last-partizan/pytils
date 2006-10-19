# -*- coding: utf-8 -*-
# License: GNU GPL2
# Author: Pythy <the.pythy@gmail.com>
"""
pytils.dt templatetags for Django web-framework
"""

__id__ = __revision__ = "$Id$"
__url__ = "$URL$"

import time
from django import template, conf
from pytils import dt, utils

register = template.Library()
encoding = conf.settings.DEFAULT_CHARSET
debug = conf.settings.DEBUG
show_value = getattr(conf.settings, 'PYTILS_SHOW_VALUES_ON_ERROR', False)

# Если отладка, то показываем 'unknown+сообщение об ошибке'.
# Если отладка выключена, то можно чтобы при ошибках показывалось
# значение, переданное фильтру (PYTILS_SHOW_VALUES_ON_ERROR=True)
# либо пустая строка.

if debug:
    default_value = "unknown: %(error)s"
    default_uvalue = u"unknown: %(error)s"
elif show_value:
    default_value = "%(value)s"
    default_uvalue = u"%(value)s"
else:
    default_value = ""
    default_uvalue = u""

# -- filters --

def distance_of_time(from_time, accuracy=1):
    """
    Display distance of time from current time.

    Parameter is an accuracy level (deafult is 1).
    Value must be numeral (i.e. time.time() result) or
    datetime.datetime (i.e. datetime.datetime.now()
    result).

    Examples::
        {{ some_time|distance_of_time }}
        {{ some_dtime|distance_of_time:2 }}
    """
    try:
        res = utils.provide_str(
            dt.distance_of_time_in_words(from_time, accuracy),
            encoding,
            default=default_value)
    except Exception, err:
        # because filter must die silently
        try:
            default_distance = "%s seconds" % str(int(time.time() - from_time))
        except Exception:
            default_distance = ""
        res = default_value % {'error': err, 'value': default_distance}
    return res

def ru_strftime(date, format="%d.%m.%Y", inflected_day=False):
    """
    Russian strftime, formats date with given format.

    Value is a date (supports datetime.date and datetime.datetime),
    parameter is a format (string). For explainings about format,
    see documentation for original strftime:
    http://docs.python.org/lib/module-time.html

    Examples::
        {{ some_date|ru_strftime:"%d %B %Y, %A" }}
    """
    try:
        uformat = utils.provide_unicode(format, encoding, default=u"%d.%m.%Y")
        ures = dt.ru_strftime(uformat,
                              date,
                              inflected=True,
                              inflected_day=inflected_day)
        res = utils.provide_str(ures, encoding)
    except Exception, err:
        # because filter must die silently
        try:
            default_date = date.strftime(format)
        except Exception:
            default_date = ""
        res = default_value % {'error': err, 'value': default_date}
    return res

def ru_strftime_inflected(date, format="%d.%m.%Y", inflected_day=True):
    """
    Russian strftime with inflected day, formats date
    with given format (similar to ru_strftime),
    also inflects day in proper form.

    Examples::
        {{ some_date|ru_strftime_inflected:"in %A (%d %B %Y)"
    """
    return ru_strftime(date, format, inflected_day)

# -- register filters
register.filter('distance_of_time', distance_of_time)
register.filter('ru_strftime', ru_strftime)
register.filter('ru_strftime_inflected', ru_strftime_inflected)
