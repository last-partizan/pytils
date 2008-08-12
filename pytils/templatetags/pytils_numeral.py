# -*- coding: utf-8 -*-
# -*- test-case-name: pytils.test.templatetags.test_numeral -*-
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
pytils.numeral templatetags for Django web-framework
"""

from django import template, conf
from pytils import numeral, utils
from pytils.templatetags import pseudo_str, pseudo_unicode, init_defaults

register = template.Library()  #: Django template tag/filter registrator
encoding = conf.settings.DEFAULT_CHARSET  #: Current charset (sets in Django project's settings)
debug = conf.settings.DEBUG  #: Debug mode (sets in Django project's settings)
show_value = getattr(conf.settings, 'PYTILS_SHOW_VALUES_ON_ERROR', False)  #: Show values on errors (sets in Django project's settings)

default_value, default_uvalue = init_defaults(debug, show_value)

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
        if isinstance(variants, basestring):
            uvariants = pseudo_unicode(variants, encoding, default_value)
        else:
            uvariants = [pseudo_unicode(v, encoding, default_uvalue) for v in variants]
        ures = numeral.choose_plural(amount, uvariants)
        res = pseudo_str(
                ures,
                encoding,
                default_value
                )
    except Exception, err:
        # because filter must die silently
        try:
            default_variant = variants
        except Exception:
            default_variant = ""
        res = default_value % {'error': err, 'value': default_variant}
    return res

def get_plural(amount, variants):
    """
    Get proper form for plural and it value.

    Value is a amount, parameters are forms of noun.
    Forms are variants for 1, 2, 5 nouns. It may be tuple
    of elements, or string where variants separates each other
    by comma. You can append 'absence variant' after all over variants

    Examples::
        {{ some_int|get_plural:"пример,примера,примеров,нет примеров" }}
    """
    try:
        if isinstance(variants, basestring):
            uvariants = pseudo_unicode(variants, encoding, default_value)
        else:
            uvariants = [pseudo_unicode(v, encoding, default_uvalue) for v in variants]
        ures = numeral._get_plural_legacy(amount, uvariants)
        res = pseudo_str(
            ures,
            encoding,
            default_value
            )
    except Exception, err:
        # because filter must die silently
        try:
            default_variant = variants
        except Exception:
            default_variant = ""
        res = default_value % {'error': err, 'value': default_variant}
    return res

def rubles(amount, zero_for_kopeck=False):
    """Converts float value to in-words representation (for money)"""
    try:
        ures = numeral.rubles(amount, zero_for_kopeck)
        res = pseudo_str(
            ures,
            encoding,
            default_value
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
        ures = numeral.in_words(amount, getattr(numeral, str(gender), None))
        res = pseudo_str(
                ures,
                encoding,
                default_value
            )
    except Exception, err:
        # because filter must die silently
        res = default_value % {'error': err, 'value': str(amount)}
    return res

# -- register filters

register.filter('choose_plural', choose_plural)
register.filter('get_plural', get_plural)
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
        if isinstance(items, basestring):
            uitems = pseudo_unicode(items, encoding, default_uvalue)
        else:
            uitems = [pseudo_unicode(i, encoding, default_uvalue) for i in items]
        ures = numeral.sum_string(amount, getattr(numeral, str(gender), None), uitems)
        res = pseudo_str(
                ures,
                encoding,
                default_value
            )
    except Exception, err:
        # because tag's renderer must die silently
        res = default_value % {'error': err, 'value': str(amount)}
    return res

# -- register tags

register.simple_tag(sum_string)
