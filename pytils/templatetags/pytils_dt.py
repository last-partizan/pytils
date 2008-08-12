# -*- coding: utf-8 -*-
# -*- test-case-name: pytils.test.templatetags.test_dt -*- 
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
pytils.dt templatetags for Django web-framework
"""

import time
from django import template, conf
from pytils import dt, utils
from pytils.templatetags import pseudo_str, pseudo_unicode, init_defaults

register = template.Library()  #: Django template tag/filter registrator
encoding = conf.settings.DEFAULT_CHARSET  #: Current charset (sets in Django project's settings)
debug = conf.settings.DEBUG  #: Debug mode (sets in Django project's settings)
show_value = getattr(conf.settings, 'PYTILS_SHOW_VALUES_ON_ERROR', False)  #: Show values on errors (sets in Django project's settings)

default_value, default_uvalue = init_defaults(debug, show_value)

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
        ures = dt.distance_of_time_in_words(from_time, accuracy)
        res = pseudo_str(
                ures,
                encoding,
                default_value)
    except Exception, err:
        # because filter must die silently
        try:
            default_distance = "%s seconds" % str(int(time.time() - from_time))
        except Exception:
            default_distance = ""
        res = default_value % {'error': err, 'value': default_distance}
    return res

def ru_strftime(date, format="%d.%m.%Y", inflected_day=False, preposition=False):
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
        uformat = pseudo_unicode(format, encoding, u"%d.%m.%Y")
        ures = dt.ru_strftime(uformat,
                              date,
                              inflected=True,
                              inflected_day=inflected_day,
                              preposition=preposition)
        res = pseudo_str(ures, encoding)
    except Exception, err:
        # because filter must die silently
        try:
            default_date = date.strftime(format)
        except Exception:
            default_date = str(date)
        res = default_value % {'error': err, 'value': default_date}
    return res

def ru_strftime_inflected(date, format="%d.%m.%Y"):
    """
    Russian strftime with inflected day, formats date
    with given format (similar to ru_strftime),
    also inflects day in proper form.

    Examples::
        {{ some_date|ru_strftime_inflected:"in %A (%d %B %Y)"
    """
    return ru_strftime(date, format, inflected_day=True)

def ru_strftime_preposition(date, format="%d.%m.%Y"):
    """
    Russian strftime with inflected day and correct preposition,
    formats date with given format (similar to ru_strftime),
    also inflects day in proper form and inserts correct 
    preposition.

    Examples::
        {{ some_date|ru_strftime_prepoisiton:"%A (%d %B %Y)"
    """
    return ru_strftime(date, format, preposition=True)


# -- register filters
register.filter('distance_of_time', distance_of_time)
register.filter('ru_strftime', ru_strftime)
register.filter('ru_strftime_inflected', ru_strftime_inflected)
register.filter('ru_strftime_preposition', ru_strftime_preposition)
