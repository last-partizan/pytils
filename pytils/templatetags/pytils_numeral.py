# -*- coding: utf-8 -*-
# License: GNU GPL2
# Author: Pythy <the.pythy@gmail.com>
"""
pytils.numeral templatetags for Django web-framework
"""

__id__ = __revision__ = "$Id$"
__url__ = "$URL$"

from django import template, conf
from pytils import numeral, utils

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
    
# -- filters

def choose_plural(amount, variants):
    """Choose proper form for plural"""
    
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
    """Convert float value to in-words representation (for money)"""
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
    """In-words representation of amount"""
    try:
        res = utils.provide_str(
            numeral.in_words(amount, gender),
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
    """in_words and choose_plural in a one flask"""
    try:
        uitems = [utils.provide_unicode(i, encoding, default_uvalue) for i in items]
        res = utils.provide_str(
            numeral.sum_string(amount, gender, uitems),
            encoding,
            default=default_value
            )
    except Exception, err:
        # because tag's renderer must die silently
        res = default_value % {'error': err, 'value': str(amount)}
    return res

# -- register tags

register.simple_tag(sum_string)    
