# -*- coding: utf-8 -*-
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
pytils.numeral templatetags for Django web-framework
"""

__id__ = __revision__ = "$Id$"
__url__ = "$URL$"

from django import template, conf
from pytils import numeral, utils

register = template.Library()  #: Django template tag/filter registrator
encoding = conf.settings.DEFAULT_CHARSET  #: Current charset (sets in Django project's settings)
debug = conf.settings.DEBUG  #: Debug mode (sets in Django project's settings)
show_value = getattr(conf.settings, 'PYTILS_SHOW_VALUES_ON_ERROR', False)  #: Show values on errors (sets in Django project's settings)

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
    
# -- filters

def choose_plural(amount, variants):
    """
    Choose proper form for plural.

    Value is a amount, parameters are forms of noun.
    Forms are variants for 1, 2, 5 nouns. It may be tuple
    of elements, or string where variants separates each other
    by comma.

    Examples::
        {{ some_int|choose_plural:"пример,примера,примеров" }}
    """
    try:
        if isinstance(variants, str):
            uvariants = utils.provide_unicode(variants, encoding, default_value)
        else:
            uvariants = [utils.provide_unicode(v, encoding, default_uvalue) for v in variants]
        res = utils.provide_str(
            numeral.choose_plural(amount, uvariants),
            encoding,
            default=default_value
            )
    except Exception, err:
        # because filter must die silently
        try:
            default_variant = variants[0]
        except Exception:
            default_variant = ""
        res = default_value % {'error': err, 'value': default_variant}
    return res

def rubles(amount, zero_for_kopeck=False):
    """Converts float value to in-words representation (for money)"""
    try:
        res = utils.provide_str(
            numeral.rubles(amount, zero_for_kopeck),
            encoding,
            default=default_value
            )
    except Exception, err:
        # because filter must die silently
        res = default_value % {'error': err, 'value': str(amount)}
    return res

def in_words(amount, gender=None):
    """
    In-words representation of amount.

    Parameter is a gender: MALE, FEMALE or NEUTER

    Examples::
        {{ some_int|in_words }}
        {{ some_other_int|in_words:FEMALE }}
    """
    try:
        res = utils.provide_str(
            numeral.in_words(amount, getattr(numeral, str(gender), None)),
            encoding,
            default=default_value
            )
    except Exception, err:
        # because filter must die silently
        res = default_value % {'error': err, 'value': str(amount)}
    return res

# -- register filters

register.filter('choose_plural', choose_plural)
register.filter('rubles', rubles)
register.filter('in_words', in_words)

# -- tags

def sum_string(amount, gender, items):
    """
    in_words and choose_plural in a one flask
    Makes in-words representation of value with
    choosing correct form of noun.

    First parameter is an amount of objects. Second is a
    gender (MALE, FEMALE, NEUTER). Third is a variants
    of forms for object name.

    Examples::
        {% sum_string some_int MALE "пример,примера,примеров" %}
        {% sum_string some_other_int FEMALE "задача,задачи,задач" %}
    """
    try:
        uitems = [utils.provide_unicode(i, encoding, default_uvalue) for i in items]
        res = utils.provide_str(
            numeral.sum_string(amount, getattr(numeral, str(gender), None), uitems),
            encoding,
            default=default_value
            )
    except Exception, err:
        # because tag's renderer must die silently
        res = default_value % {'error': err, 'value': str(amount)}
    return res

# -- register tags

register.simple_tag(sum_string)
