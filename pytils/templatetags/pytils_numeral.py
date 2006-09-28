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

# -- filters

def choose_plural(amount, variants):
    """Choose proper form for plural"""
    try:
        uvariants = [utils.provide_unicode(v, encoding) for v in variants]
        res = utils.provide_str(numeral.choose_plural(amount, uvariants), encoding)
    except Exception:
        # because filter must die silently
        res = "unknown"
    return res

def rubles(amount, zero_for_kopeck=False):
    """Convert float value to in-words representation (for money)"""
    try:
        res = utils.provide_str(numeral.rubles(amount, zero_for_kopeck), encoding)
    except Exception:
        # because filter must die silently
        res = "unknown"
    return res

def in_words(amount, gender=None):
    """In-words representation of amount"""
    try:
        res = utils.provide_str(numeral.in_words(amount, gender), encoding)
    except Exception:
        # because filter must die silently
        res = "unknown"
    return res        
            
# -- register filters

register.filter('choose_plural', choose_plural)
register.filter('rubles', rubles)
register.filter('in_words', in_words)

# -- tags

def sum_string(amount, gender, items):
    try:
        uitems = [utils.provide_unicode(i, encoding) for i in items]
        res = utils.provide_str(
            numeral.sum_string(amount, gender, uitems),
            encoding
        )
    except Exception:
        # because renderer mus die silently
        res = "unknown"
    return res

# -- register tags

register.simple_tag(sum_string)    
