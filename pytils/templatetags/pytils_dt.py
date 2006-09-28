# -*- coding: utf-8 -*-
# License: GNU GPL2
# Author: Pythy <the.pythy@gmail.com>
"""
pytils.dt templatetags for Django web-framework
"""

__id__ = __revision__ = "$Id$"
__url__ = "$URL$"

from django import template, conf
from pytils import dt, utils

register = template.Library()
encoding = conf.settings.DEFAULT_CHARSET

# -- filters --

def distance_of_time(from_time, accuracy=1):
    """Display distance of time from current time"""
    try:
        res = utils.provide_str(
            dt.distance_of_time_in_words(from_time, accuracy),
            encoding)
    except Exception:
        # because filter must die silently
        res = "unknown"
    return res

def ru_strftime(date, format="%d.%m.%Y", inflected_day=False):
    """Russian strftime"""
    try:
        uformat = utils.provide_unicode(format, encoding, default=u"%d.%m.%Y")
        ures = dt.ru_strftime(uformat,
                              date,
                              inflected=True,
                              inflected_day=inflected_day)
        res = utils.provide_str(ures, encoding)
    except Exception:
        # because filter must die silently
        res = "unknown"
    return res

def ru_strftime_inflected(date, format="%d.%m.%Y", inflected_day=True):
    """Russian strftime with inflected day"""
    return ru_strftime(date, format, inflected_day)

# -- register filters
register.filter('distance_of_time', distance_of_time)
register.filter('ru_strftime', ru_strftime)
register.filter('ru_strftime_inflected', ru_strftime_inflected)
